#!/usr/bin/env python3
"""adding async comprehension coroutine"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async comprehension that collects numbers generated"""
    # THIS IS A COMPREHENSION!!!!!!!!!!!!!!!!!!!
    numbers = [number async for number in async_generator()]
    return numbers
