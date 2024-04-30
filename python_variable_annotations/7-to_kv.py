#!/usr/bin/env python3
"""complex types converting string and int/float to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes string and number and returns tuple with both"""
    return (k, v * v)
