import asyncio
from datetime import datetime, timedelta
from queue import Queue, Empty
from threading import Thread, Lock
import threading
import time
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_candidate = 0
prime_lock = Lock()
last_prime = None

def get_next_prime_candidate():
    global prime_candidate
    with prime_lock:
        current = prime_candidate
        prime_candidate += 1
        return current

def worker(time_limit):
    global last_prime
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=time_limit)

    while datetime.now() < end_time:
        candidate = get_next_prime_candidate()
        if is_prime(candidate):
            last_prime = candidate
            print(f"Prime number found by Thread {threading.current_thread().name}: {last_prime} at {datetime.now().strftime('%H:%M:%S.%f')}")
        time.sleep(0.001)  # Small sleep to avoid busy-waiting

def threaded_pool(time_limit, num_threads):
    threads = [
        Thread(target=worker, args=(time_limit,))
        for _ in range(num_threads)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return last_prime

async def main():
    global last_prime
    THREAD_POOL_SIZE = 32
    TIME_LIMIT = 3 * 60  # Set the time limit for the threaded operation in seconds

    print(f"Number of threads before start: {threading.active_count()}\n\n\n")

    start = datetime.now()
    final_prime = threaded_pool(TIME_LIMIT, THREAD_POOL_SIZE)
    end = datetime.now()

    print("----------------")
    total_time = end - start
    print(f"Total Time (Threaded): {total_time.total_seconds():.2f}s")
    print(f"Last Prime Number Found: {final_prime}")

if __name__ == "__main__":
    asyncio.run(main())