#!/usr/bin/env python3
"""duck type for an iterable object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """duck typing for an iterable object"""
    return [(i, len(i)) for i in lst]
