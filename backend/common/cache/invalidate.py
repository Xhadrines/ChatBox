from .policies import (
    invalidate_chat_policy_cache,
    invalidate_file_policy_cache,
    invalidate_admin_cache,
)


def invalidate_all_policy_caches(
    user_id: int | None = None, service_name: str | None = None, pk: int | None = None
):
    invalidate_chat_policy_cache(user_id)
    invalidate_file_policy_cache(user_id)
    invalidate_admin_cache(service_name=service_name, pk=pk)
