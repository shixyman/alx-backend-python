#!/usr/bin/env python3
""" Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    Notice that the total runtime is roughly 10 seconds,
    explain it to yourself. """
import asyncio
from file_with_async_comprehension import async_comprehension


async def measure_runtime():
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = asyncio.get_event_loop().time()
    runtime = end_time - start_time

    return runtime
