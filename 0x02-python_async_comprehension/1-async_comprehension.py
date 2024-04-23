#!/usr/bin/env python3
""" Import async_generator from the previous task and then write a coroutine
    called async_comprehension that takes no arguments.
    The coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers. """
from previous_file import async_generator


async def async_comprehension():
    random_numbers = [number async for number in async_generator()]
    return random_numbers
