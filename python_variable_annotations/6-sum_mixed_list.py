#!/usr/bin/env python3
"""mixed type list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns float sum of mixed type list"""
    return sum(mxd_lst)
