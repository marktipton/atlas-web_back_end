#!/usr/bin/env python3
"""Using regular (non-async) function """
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns the asyncio.Task of the wait_random function"""
    wait_random(max_delay)