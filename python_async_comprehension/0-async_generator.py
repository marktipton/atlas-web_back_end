#!/usr/bin/env python3
"""coroutine that creates 10 random numbers between 1 and 10"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """coroutine that creates 10 random numbers between 1 and 10"""

    # random_number_list = []
    i: int = 0
    while (i < 10):
        i += 1
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
