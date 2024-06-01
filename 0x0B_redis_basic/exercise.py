#!/usr/bin/env python3
"""
Exercise operations Redis
"""
from functools import wraps
import redis
import uuid
from typing import Union, Callable, Optional, Any


def count_calls(method: Callable) -> Callable:
    """decorator function to count calls of another function or class"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper"""
        cls = self.__class__
        # initialize _call_counts attribute if it does not exist in class
        if not hasattr(cls, '_call_counts'):
            # dictionary for storing call counts for each method
            cls._call_counts = {}
        # check if qualified name is not already a key
        # in the _call_counts dictionary
        if method.__qualname__ not in cls._call_counts:
            # since the qualname is not in the dictioanry, init its count to 0
            cls._call_counts[method.__qualname__] = 0
        # otherwise, qualname is in the dictionary
        # so increment the value to count call
        cls._call_counts[method.__qualname__] += 1
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """redis caching"""
    def __init__(self):
        # store instance of redis client
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        # flush instance
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key and stores"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[Any]:
        """used to convert data back from byte string"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """parameterize Cache.get with str conversion"""
        return self.get(key, lambda a: a.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """parameterize Cache.get with int conversion"""
        return self.get(key, lambda a: int(a))
