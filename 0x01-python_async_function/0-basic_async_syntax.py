#!/usr/bin/env python3
""" Module for a function to create delay """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ The function that waits for a random delay """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
