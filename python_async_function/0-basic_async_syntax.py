#!/usr/bin/env python3
"""Basic Async Operation"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for random delay and eventually returns value"""
    wait_time = random.random(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
