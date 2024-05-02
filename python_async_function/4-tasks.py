#!/usr/bin/env python3
"""Changing wait_n into task_wait_n"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """creates n wait_random functions with specified max_delay"""
    wait_times = []

    # create list of coroutine tasks
    tasks = [task_wait_random(max_delay) for i in range(n)]

    # Await completion of tasks as completed
    for task in asyncio.as_completed(tasks):
        wait_time = await task
        wait_times.append(wait_time)

    return wait_times
