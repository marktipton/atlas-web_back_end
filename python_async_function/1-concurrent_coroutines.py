#!/usr/bin/env python3
"""Use wait_random function and make function to spawn n wait_randoms"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """creates n wait_random functions with specified max_delay"""
    for i in range(n):
        asyncio.run(wait_random(max_delay))
        print()


