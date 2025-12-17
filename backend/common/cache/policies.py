from django.core.cache import cache

ADMIN_CACHE_TTL = 300

CHAT_POLICY_TTL = 300
FILE_POLICY_TTL = 300


def _admin_cache_key(service_name: str, pk: int | None):
    return f"admin:get:{service_name}:{pk or 'all'}"


def get_admin_cache(service_name: str, pk: int | None = None):
    return cache.get(_admin_cache_key(service_name, pk))


def set_admin_cache(service_name: str, data, pk: int | None = None):
    cache.set(_admin_cache_key(service_name, pk), data, timeout=ADMIN_CACHE_TTL)


def invalidate_admin_cache(service_name: str | None = None, pk: int | None = None):
    if service_name and pk is not None:
        cache.delete(_admin_cache_key(service_name, pk))
    elif service_name:
        cache.clear()
    else:
        cache.clear()


def _chat_policy_key(user_id: int) -> str:
    return f"chat_policy:{user_id}"


def _file_policy_key(user_id: int) -> str:
    return f"file_policy:{user_id}"


def get_chat_policy_cache(user_id: int):
    return cache.get(_chat_policy_key(user_id))


def set_chat_policy_cache(user_id: int, data: dict):
    cache.set(
        _chat_policy_key(user_id),
        data,
        timeout=CHAT_POLICY_TTL,
    )


def invalidate_chat_policy_cache(user_id: int | None = None):
    if user_id is not None:
        cache.delete(_chat_policy_key(user_id))
    else:
        cache.clear()


def get_file_policy_cache(user_id: int):
    return cache.get(_file_policy_key(user_id))


def set_file_policy_cache(user_id: int, data: dict):
    cache.set(
        _file_policy_key(user_id),
        data,
        timeout=FILE_POLICY_TTL,
    )


def invalidate_file_policy_cache(user_id: int | None = None):
    if user_id is not None:
        cache.delete(_file_policy_key(user_id))
    else:
        cache.clear()
