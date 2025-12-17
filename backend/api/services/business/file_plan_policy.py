import logging
from django.utils import timezone

from common.cache.policies import get_file_policy_cache, set_file_policy_cache


logger = logging.getLogger(__name__)


class FilePlanPolicy:
    def __init__(self, user_plans_accessor):
        self.user_plans_accessor = user_plans_accessor

    def resolve_file_policy(self, user):
        cached = get_file_policy_cache(user.id)
        if cached:
            logger.info(f"[CACHE] Using file policy cache for UserID {user.id}")
            return cached, None

        now = timezone.now()

        user_plans = self.user_plans_accessor.get_by_user(user.id)

        active_plans = [
            p
            for p in user_plans
            if p.start_date <= now and (p.end_date is None or p.end_date >= now)
        ]

        if not active_plans:
            logger.warning(f"[FILE POLICY] UserID: {user.id} | No active plan")
            return None, "Userul nu are plan activ"

        active_plan = sorted(
            active_plans,
            key=lambda p: (p.end_date is not None, p.end_date),
            reverse=True,
        )[0]

        daily_file_limit = getattr(active_plan.plan, "daily_file_limit", None)

        result = {
            "active_plan": active_plan,
            "daily_file_limit": daily_file_limit,
        }

        set_file_policy_cache(user.id, result)
        logger.info(f"[CACHE] Created file policy cache for UserID {user.id}")

        logger.info(
            f"[FILE POLICY] UserID: {user.id} | Active Plan: {active_plan.plan.name} | Daily limit: {daily_file_limit}"
        )

        return result, None
