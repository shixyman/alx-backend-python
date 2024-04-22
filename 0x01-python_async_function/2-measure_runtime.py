#!/usr/bin/env python3
"""Contains a method that measure the total execution time of
a function"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()

    # Measure the total execution time for wait_n
    delays: List[float] = asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate the average time per execution
    average_time = total_time / n

    return average_time