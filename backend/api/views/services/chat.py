from rest_framework.views import APIView
from rest_framework.response import Response
import ollama
from django.utils import timezone
import os
import pdfplumber

from ...data_access.messages import MessagesAccessor
from ...data_access.users import UsersAccessor
from ...data_access.user_plans import UserPlansAccessor
from ...data_access.files import FilesAccessor
from ...serializers.messages import MessagesSerializer


class ChatView(APIView):
    accessor = MessagesAccessor()
    user_accessor = UsersAccessor()
    user_plans_accessor = UserPlansAccessor()
    files_accessor = FilesAccessor()

    MODEL_MAPPING = {
        "gpt-oss": "gpt-oss:20b",
        "llama3.2": "llama3.2",
    }

    def get_user_files_content(self, user_id):
        files = self.files_accessor.get_all().filter(user_id=user_id)
        content = ""
        for file in files:
            file_path = file.file_path
            if not os.path.exists(file_path):
                continue
            ext = file.file_name.split(".")[-1].lower()
            try:
                if ext == "txt":
                    with open(file_path, "r", encoding="utf-8") as f:
                        content += f"[File: {file.file_name}]\n{f.read()}\n"
                elif ext == "pdf":
                    with pdfplumber.open(file_path) as pdf:
                        text = "\n".join(
                            page.extract_text() or "" for page in pdf.pages
                        )
                        content += f"[File: {file.file_name}]\n{text}\n"
            except Exception as e:
                print(f"Error reading file {file.file_name}: {e}")
        return content

    def post(self, request, user_id=None):
        user = self.user_accessor.get_by_id(user_id)
        if not user:
            return Response({"error": "User not found"}, status=404)

        prompt = request.data.get("prompt", "")
        if not prompt:
            return Response({"error": "Prompt is required"}, status=400)

        now = timezone.now()
        user_plans = self.user_plans_accessor.get_by_user(user.id)
        active_plan = next(
            (p for p in user_plans if p.end_date is None or p.end_date >= now), None
        )
        if not active_plan:
            return Response({"error": "No active plan"}, status=403)

        gpt_oss_limit = getattr(active_plan.plan, "daily_prm_msg", None)
        gpt_oss_count_today = self.accessor.count_messages_today(user, "gpt-oss:20b")

        model_key = (
            "gpt-oss"
            if gpt_oss_limit is None or gpt_oss_count_today < gpt_oss_limit
            else getattr(active_plan.plan, "name_llm_std", "llama3.2")
        )
        if model_key == "gpt-oss":
            gpt_oss_count_today += 1
        model_to_use = self.MODEL_MAPPING.get(model_key, "llama3.2")

        try:

            messages_history = self.accessor.get_by_user_id(user.id)
            conversation_context = ""
            for msg in messages_history:
                if msg.user_msg:
                    conversation_context += f"[User] {msg.user_msg}\n"
                if msg.llm_resp:
                    conversation_context += f"[AI] {msg.llm_resp}\n"

            files_context = self.get_user_files_content(user.id)

            user_context = (
                f"User info:\n"
                f"Username: {user.username}\n"
                f"Email: {user.email}\n"
                f"Plan: {active_plan.plan.name}\n"
            )

            full_prompt = (
                user_context
                + "\n"
                + files_context
                + "\n"
                + conversation_context
                + f"[User] {prompt}\n[AI]"
            )

            print(model_to_use)
            result = ollama.generate(model=model_to_use, prompt=full_prompt)
            llm_response = result.get("response", "")

            new_message = self.accessor.add(
                user=user,
                user_msg=prompt,
                llm_resp=llm_response,
                llm_used=model_to_use,
            )

            remaining = (
                None
                if gpt_oss_limit is None
                else max(0, gpt_oss_limit - gpt_oss_count_today)
            )

            return Response(
                {
                    "response": llm_response,
                    "saved_message": MessagesSerializer(new_message).data,
                    "model_used": model_to_use,
                    "gpt_oss_remaining": remaining,
                    "active_plan_id": active_plan.id,
                },
                status=200,
            )
        except Exception as e:
            print("Exception in ChatView POST:", e)
            return Response({"error": str(e)}, status=500)
