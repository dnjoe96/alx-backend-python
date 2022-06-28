#!/usr/bin/env python3
""" Module for async_generator function """
import asyncio
import random


async def async_generator():
    """ Function to generate async delay"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        # await asyncio.sleep(1)
