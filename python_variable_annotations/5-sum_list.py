#!/usr/bin/env python3
"""return sum of list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """returns sum of list of floats"""
    total: float
    for floats in input_list:
        total += floats
    return total
