#!/usr/bin/env python3
"""Use wait_random function and make function to spawn n wait_randoms"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """creates n wait_random functions with specified max_delay"""
    wait_times = []

    # create list of coroutine tasks
    tasks = [wait_random(max_delay) for i in range(n)]

    # Await completion of tasks as completed
    for task in asyncio.as_completed(tasks):
        wait_time = await task
        wait_times.append(wait_time)

    return wait_times
