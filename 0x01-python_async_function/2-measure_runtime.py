#!/usr/bin/env python3
""" Module for measure_time function """
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Function measures the average time for the responses"""
    respList = asyncio.run(wait_n(n, max_delay))
    return sum(respList) / len(respList)
