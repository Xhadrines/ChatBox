from datetime import timedelta
from django.utils import timezone

from common.models.messages import Messages


class MessagesAccessor:
    def add(self, user, user_msg, llm_resp, llm_used):
        message = Messages(
            user=user,
            user_msg=user_msg,
            llm_resp=llm_resp,
            llm_used=llm_used,
        )
        message.save()
        return message

    def get_all(self):
        return Messages.objects.all()

    def get_by_id(self, message_id):
        try:
            return Messages.objects.get(id=message_id)
        except Messages.DoesNotExist:
            return None

    def get_by_user_id(self, user_id):
        return Messages.objects.filter(user__id=user_id).order_by("id")

    def update(self, message_id, **kwargs):
        try:
            message = Messages.objects.get(id=message_id)
        except Messages.DoesNotExist:
            return None

        for key, value in kwargs.items():
            setattr(message, key, value)
        message.save()
        return message

    def delete(self, message_id):
        deleted, _ = Messages.objects.filter(id=message_id).delete()
        return deleted

    def count_messages_today(self, user, llm_used):
        today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        return Messages.objects.filter(
            user=user,
            llm_used=llm_used,
            uploaded_at__gte=today_start,
            uploaded_at__lt=today_end,
        ).count()
