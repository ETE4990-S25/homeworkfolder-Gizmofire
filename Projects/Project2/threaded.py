
import asyncio
# from asyncio import TaskGroup
from datetime import datetime, timedelta


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


async def print_number(time):
    x = 0 
    start_time = datetime.now()  # Get the current time
    end_time = start_time + timedelta(seconds=time)  # Set the deadline to 3 seconds from now

    while datetime.now() < end_time:  # Loop until the deadline is reached
        if is_prime(x):
           print(f"Prime number: {x}")
        x += 1
        await asyncio.sleep(0.01)


async def main():
    task1 = asyncio.create_task(print_number(3 * 60))
    await task1

asyncio.run(main())
