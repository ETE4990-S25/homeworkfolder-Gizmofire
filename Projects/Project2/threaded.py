import asyncio
# sample code to test asyncio
async def print_numbers():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(1)
        #time.sleep(1)

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_numbers())

asyncio.run(main())