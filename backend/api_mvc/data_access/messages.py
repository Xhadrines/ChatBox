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
