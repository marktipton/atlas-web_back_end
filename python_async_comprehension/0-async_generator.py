#!/usr/bin/env python3
"""coroutine that creates 10 random numbers between 1 and 10"""

import asyncio
import random
from typing import List

async def async_generator() -> List[int]:
    random_number_list = []
    i = 0
    while (i < 10):
        i += 1
        await asyncio.sleep(1)
        random_number_list += random.uniform(0, 10)

    return random_number_list
