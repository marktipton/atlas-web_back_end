#!/usr/bin/env python3
"""complex types converting string and int/float to tuple"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """takes string and number and returns tuple with both"""
    return tuple(k, v)
