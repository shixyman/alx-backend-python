#!/usr/bin/env python3
"""Contains a method that spawns Tasks n times with a
specified delay between each call."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

# Import task_wait_random from the previous code
from file_with_task_wait_random import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    delays = []

    # Create a list of tasks for task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Gather the results of all tasks
    results = await asyncio.gather(*tasks)

    # Sort the results in ascending order
    delays = sorted(results)

    return delays