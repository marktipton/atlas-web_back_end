#!/usr/bin/env python3
"""
Exercise operations Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """redis caching"""
    def __init__(self) -> None:
        # store instance of redis client
        _redis = redis.Redis()
        # flush instance
        _redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generates a random key and stores"""
        random_key = uuid.uuid4()
