#!/usr/bin/env python3
""" Module for async_generator function """
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """ The function returns a list of radom numbers from
    async_generator function
    """
    return [num async for num in async_generator()]
