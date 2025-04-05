import asyncio

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Define an asynchronous function to print numbers
async def print_number(number):
    print(number + ": " + str(is_prime(number)))  # Print the number and its primality

# Set up the loop and run the coroutine
loop = asyncio.get_event_loop()  # Get the current event loop
loop.run_until_complete(  # Run the event loop until the coroutines finish
    asyncio.gather(*(print_number(num) for num in range(1000000)))
)
loop.close()  # 