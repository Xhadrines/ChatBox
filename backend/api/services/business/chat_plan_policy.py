from django.utils import timezone
import logging

from common.cache.policies import get_chat_policy_cache, set_chat_policy_cache


logger = logging.getLogger(__name__)


class ChatPlanPolicy:
    def __init__(self, user_plans_accessor, messages_accessor, model_mapping):
        self.user_plans_accessor = user_plans_accessor
        self.messages_accessor = messages_accessor
        self.model_mapping = model_mapping

    def resolve_chat_policy(self, user):
        cached = get_chat_policy_cache(user.id)
        if cached:
            logger.info(f"[CACHE] Using chat policy cache for UserID {user.id}")
            return cached, None

        now = timezone.now()

        user_plans = self.user_plans_accessor.get_by_user(user.id)
        active_plans = [
            p
            for p in user_plans
            if p.start_date <= now and (p.end_date is None or p.end_date >= now)
        ]

        if not active_plans:
            logger.warning(f"[CHAT POLICY] UserID: {user.id} | No active plan")
            return None, "No active plan"

        active_plan = sorted(
            active_plans,
            key=lambda p: (p.end_date is not None, p.end_date),
            reverse=True,
        )[0]

        gpt_oss_limit = getattr(active_plan.plan, "daily_prm_msg", None)

        gpt_oss_count_today = self.messages_accessor.count_messages_today(
            user, "gpt-oss:20b"
        )

        if gpt_oss_limit is None or gpt_oss_count_today < gpt_oss_limit:
            model_key = "gpt-oss"
            gpt_oss_count_today += 1
        else:
            model_key = getattr(active_plan.plan, "name_llm_std", "llama3.2")

        model_to_use = self.model_mapping.get(model_key, "llama3.2")

        remaining = (
            None
            if gpt_oss_limit is None
            else max(0, gpt_oss_limit - gpt_oss_count_today)
        )

        result = {
            "active_plan": active_plan,
            "model_key": model_key,
            "model_to_use": model_to_use,
            "remaining": remaining,
        }

        set_chat_policy_cache(user.id, result)
        logger.info(f"[CACHE] Created chat policy cache for UserID {user.id}")

        logger.info(
            f"[CHAT POLICY] UserID {user.id} | Active Plan: {active_plan.plan.name} | "
            f"Model: {model_key} | Remaining: {remaining}"
        )

        return result, None
