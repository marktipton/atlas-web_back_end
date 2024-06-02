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
        # increment call count in Redis
        self._redis.incr(method.__qualname__)
        # call the decorated method
        return method(self, *args, **kwds)
    return wrapper

def call_history(method: Callable) -> Callable:
    """stores the history of inputs and outputs for a function"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """wrapper"""
        r = method(self, *args, **kwds)
        return r
    return wrapper

class Cache:
    """redis caching"""
    def __init__(self):
        # store instance of redis client
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        # flush instance
        self._redis.flushdb()

    @call_history
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
