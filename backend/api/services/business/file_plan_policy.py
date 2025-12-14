import logging
from django.utils import timezone
from threading import Lock

logger = logging.getLogger(__name__)


class FilePlanPolicy:
    CACHE_TTL = 60

    def __init__(self, user_plans_accessor):
        self.user_plans_accessor = user_plans_accessor

        self._cache = {}
        self._lock = Lock()

    def resolve_file_policy(self, user):
        now = timezone.now()

        with self._lock:
            cache_entry = self._cache.get(user.id)
            if cache_entry:
                if now.timestamp() - cache_entry["timestamp"] < self.CACHE_TTL:
                    logger.info(
                        f"[CACHE] Using cached file policy for UserID {user.id}"
                    )
                    return cache_entry["data"], None
                else:
                    del self._cache[user.id]

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

        with self._lock:
            self._cache[user.id] = {"timestamp": now.timestamp(), "data": result}
            logger.info(
                f"[CACHE] Created/Updated file policy cache for UserID {user.id}"
            )

        logger.info(
            f"[FILE POLICY] UserID: {user.id} | Active Plan: {active_plan.plan.name} | Daily limit: {daily_file_limit}"
        )

        return result, None

    def invalidate_cache(self, user_id=None):
        with self._lock:
            if user_id is None:
                self._cache.clear()
            else:
                self._cache.pop(user_id, None)
        logger.info(f"[CACHE] Invalidated file policy cache for user_id={user_id}")
