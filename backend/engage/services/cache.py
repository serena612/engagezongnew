# coding: utf-8

import hashlib, functools

from cacheout import (
    CacheManager,
    LRUCache,
)

__all__ = (
    "cacheset",
    "cached",
)


## cache set goes here
cacheset = CacheManager({
    "notifications": {"cache_class": LRUCache, "maxsize": 100000, "ttl": 360, "default": None},
})


# Cache Backend
class CacheBackend(object):
    def __init__(self, manager):
        self.cache = manager

    def get(self, key):
        return self.cache.get(key, None)

    def set(self, key, value):
        self.cache.set(key, value)


# Utils
def generate_function_key(fn):
    return hashlib.md5(fn.__code__.co_code).hexdigest()


def generate_unique_key(*args, **kwargs):
    hashed_args = ["%s" % hash(arg) for arg in args]
    hashed_kwargs = ["%s " % hash((key, value)) for (key, value) in kwargs.items()]

    return hashlib.md5(":".join(hashed_args + hashed_kwargs).encode("utf-8")).hexdigest()


# Cache Decorater
def cached(manager, **kwargs):

    def decorator(fn, key=None, key_generator=None, set_kwargs=None):
        if key is None:
            key = generate_function_key(fn)

        if key_generator is None:
            key_generator = generate_unique_key

        if set_kwargs is None:
            set_kwargs = {}

        @functools.wraps(fn)
        def inner(*args, **kwargs):
            unique_key = f"{key}:{key_generator(*args, **kwargs)}"

            value = CacheBackend(manager).get(unique_key)

            if value is None:
                value = fn(*args, **kwargs)
                CacheBackend(manager).set(unique_key, value, **set_kwargs)

            return value
        return inner

    return functools.partial(decorator, **kwargs)

