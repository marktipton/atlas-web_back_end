#!/usr/bin/env python3
"""multiplies a float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns function that multiplies float by multiplier"""
    def multiplier_function(a: float) -> float:
        return a * multiplier
    return multiplier_function
