#!/usr/bin/env python3
"""measure runtime for async comprehension"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measures total runtime and returns it"""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.time()
    return (end - start)
