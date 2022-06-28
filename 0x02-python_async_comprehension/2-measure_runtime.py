#!/usr/bin/env python3
""" Module for measure_runtime function """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ The function measures the total runtime """
    start_time = time.perf_counter()
    resp = await asyncio.gather(async_comprehension(), async_comprehension(),
                                async_comprehension(), async_comprehension())
    elapsed = time.perf_counter() - start_time
    # print(elapsed)
    # print(resp)
    return elapsed
