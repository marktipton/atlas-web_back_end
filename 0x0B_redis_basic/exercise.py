#!/usr/bin/env python3
"""
Exercise operations Redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Callable = None) ->:
        """used to convert data back from byte string"""

    def get_str(self):
        """parameterize Cache.get with str conversion"""

    def get_int(self):
        """parameterize Cache.get with int conversion"""

