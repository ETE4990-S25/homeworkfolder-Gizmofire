
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




# OVER COMPLICATED CODE THAT I TRIED TO USE WITH TASK GROUPS

# taken form example https://docs.python.org/3/library/asyncio-task.html#creating-tasks
# class TerminateTaskGroup(Exception):
#     """Exception raised to terminate a task group."""

# async def force_terminate_task_group():
#     """Used to force termination of a task group."""
#     raise TerminateTaskGroup()

#  didnt work
# async def main():
#     try:
#         async with asyncio.TaskGroup() as group:
#             for i in range(1, 100000000):
#                 group.create_task(print_number(i))
#             # add an exception-raising task to force the group to terminate
#             group.create_task(force_terminate_task_group())
#     except* TerminateTaskGroup:
#         pass

# didnt work
# async def main_with_timeout():
#     try:
#         async with asyncio.timeout(3):
#             await main()
#     except asyncio.TimeoutError:
#         print("Task Group execution timed out after 10 seconds.")
#     finally:
#         print("Exiting.")

# asyncio.run(main_with_timeout())

# # DEADLINE CODE USED FOR async code
# async def main():
#     loop = get_running_loop()
#     deadline = loop.time() + 20
#     try:
#         async with asyncio.timeout_at(deadline):
#             await long_running_task()
#     except TimeoutError:
#         print("The long operation timed out, but we've handled it.")

#     print("This statement will run regardless.")




