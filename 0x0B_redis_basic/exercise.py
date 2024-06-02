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
        qualname = method.__qualname__
        input = f"{qualname}:inputs"
        output = f"{qualname}:outputs"
        # store in redis list input key w/ given args value
        self._redis.rpush(input, str(args))

        result = method(self, *args, **kwds)
        # add output key with result value,
        # (a random UUID generated by store method)
        self._redis.rpush(output, str(result))
        return result
    return wrapper


def replay(method: Callable):
    """Returns the call history for a given method"""
    qualname = method.__qualname__
    cache_instance = method.__self__
    input_key = f"{qualname}:inputs"
    output_key = f"{qualname}:outputs"
    inputs = cache_instance._redis.lrange(input_key, 0, -1)
    outputs = cache_instance._redis.lrange(output_key, 0, -1)
    history = list(zip(inputs, outputs))

    num_calls = cache_instance.get_int(qualname)

    print(f"{qualname} was called {num_calls} times:")
    for input_value, output_value in history:
        input_str = input_value.decode('utf-8')
        output_str = output_value.decode('utf-8')
        print(f"{qualname}(*{input_str}) -> {output_str}")


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
