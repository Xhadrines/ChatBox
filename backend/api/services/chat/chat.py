import os
import pdfplumber
import ollama

from django.conf import settings

from common.email.admin_logger import AdminEmailLogger

from ..business.chat_plan_policy import ChatPlanPolicy

from ...data_access.messages import MessagesAccessor
from ...data_access.files import FilesAccessor
from ...data_access.users import UsersAccessor
from ...data_access.user_plans import UserPlansAccessor

import logging

logger = logging.getLogger(__name__)


class ChatService:
    def __init__(self):
        self.messages_accessor = MessagesAccessor()
        self.files_accessor = FilesAccessor()
        self.users_accessor = UsersAccessor()
        self.user_plans_accessor = UserPlansAccessor()

        self.MODEL_MAPPING = {
            "gpt-oss": "gpt-oss:20b",
            "llama3.2": "llama3.2",
        }

        self.chat_plan_policy = ChatPlanPolicy(
            user_plans_accessor=self.user_plans_accessor,
            messages_accessor=self.messages_accessor,
            model_mapping=self.MODEL_MAPPING,
        )

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

    def get_chat_events(self, user_id):
        messages = self.messages_accessor.get_by_user_id(user_id)
        files = self.files_accessor.get_all().filter(user_id=user_id)

        events = []
        for m in messages:
            events.append(
                {
                    "type": "message",
                    "text": m.user_msg,
                    "llm_resp": m.llm_resp,
                    "llm_used": m.llm_used,
                    "created_at": m.uploaded_at,
                }
            )
        for f in files:
            events.append(
                {
                    "type": "file",
                    "file_name": f.file_name,
                    "file_url": f"{settings.MEDIA_URL}{f.user.id}/{f.file_name}",
                    "created_at": f.uploaded_at,
                }
            )
        events.sort(key=lambda x: x["created_at"])
        return events

    def send_message(self, user_id, prompt):
        logger.info(f"[CHAT ATTEMPT] UserID: {user_id} | Prompt length: {len(prompt)}")

        user = self.users_accessor.get_by_id(user_id)
        if not user:
            logger.warning(f"[CHAT FAILED] UserID: {user_id} | User not found")
            return None, "User not found"

        policy, error = self.chat_plan_policy.resolve_chat_policy(user)
        if error:
            return None, error

        active_plan = policy["active_plan"]
        model_to_use = policy["model_to_use"]
        remaining = policy["remaining"]

        messages_history = self.messages_accessor.get_by_user_id(user.id)
        conversation_context = "".join(
            f"[User] {m.user_msg}\n[AI] {m.llm_resp}\n" for m in messages_history
        )

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

        try:
            result = ollama.generate(model=model_to_use, prompt=full_prompt)
            llm_response = result.get("response", "")

            new_message = self.messages_accessor.add(
                user=user,
                user_msg=prompt,
                llm_resp=llm_response,
                llm_used=model_to_use,
            )

            logger.info(
                f"[CHAT SUCCESS] UserID: {user.id} | Model: {model_to_use} | Remaining: {remaining}"
            )

            return {
                "response": llm_response,
                "saved_message": new_message,
                "model_used": model_to_use,
                "gpt_oss_remaining": remaining,
                "active_plan_id": active_plan.id,
            }, None

        except Exception as e:
            logger.exception(
                f"[CHAT ERROR] UserID: {user.id} | Model: {model_to_use} | Prompt length: {len(prompt)} | Error: {e}"
            )

            AdminEmailLogger.send_llm_error(
                user=user,
                model=model_to_use,
                prompt=prompt,
                exception=e,
            )

            return None, f"Error during message generation: {e}"
