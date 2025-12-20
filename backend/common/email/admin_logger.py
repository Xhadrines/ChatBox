from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.utils import timezone

import logging

logger = logging.getLogger(__name__)


class AdminEmailLogger:
    @staticmethod
    def send_llm_error(*, user, model, prompt, exception):
        subject = f"🚨 ChatBox | LLM ERROR | User={user.id} | Model={model}"

        context = {
            "user": user,
            "model": model,
            "prompt": prompt,
            "prompt_length": len(prompt),
            "exception": repr(exception),
            "timestamp": timezone.now(),
        }

        text_body = f"""
                        ChatBox LLM ERROR

                        User: {user.id} ({user.username})
                        Email: {user.email}

                        Model: {model}
                        Prompt length: {len(prompt)}

                        Prompt:
                        {prompt}

                        Exception:
                        {repr(exception)}
                    """

        try:
            html_body = render_to_string("emails/llm_error.html", context)

            email = EmailMultiAlternatives(
                subject=subject,
                body=text_body,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
            )

            email.attach_alternative(html_body, "text/html")
            email.send()

            logger.info(f"[ADMIN EMAIL SENT] LLM error | UserID={user.id}")

        except Exception as e:
            logger.error(f"[ADMIN EMAIL FAILED] {e}", exc_info=True)
