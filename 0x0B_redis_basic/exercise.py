#!/usr/bin/env python3
"""
Exercise operations Redis
"""
from functools import wraps
import redis
import uuid
from typing import Union, Callable, Optional, Any


def count_calls(f: Callable) -> Callable:
    """decorator function to count calls of another function or class"""
    @wraps(f)
    def wrapper(*args, **kwds):
        """wrapper"""
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@count_calls
class Cache:
    """redis caching"""
    def __init__(self):
        # store instance of redis client
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        # flush instance
        self._redis.flushdb()

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
