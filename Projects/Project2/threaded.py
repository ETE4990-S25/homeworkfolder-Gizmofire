import asyncio
from datetime import datetime, timedelta
from queue import Queue, Empty
from threading import Thread
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

def increment():
    global counter
    global task
    with threading.Lock:  # Lock ensures only one thread modifies the counter at a time
        # print(thread.getName)
        task+=1
        print(task)
        counter += task
        print(f"Thread {threading.current_thread().name} incremented counter to {counter}")
        return counter



def print_number_sync(time_limit):
    x = increment()  # Start from the incremented value
    start_time = datetime.now()
    end_time = start_time + timedelta(seconds=time_limit)
    while datetime.now() < end_time:
        if is_prime(x):
            print(f"Prime number (Thread): {x} at {datetime.now().strftime('%H:%M:%S.%f')}")
        x += 1
        time.sleep(0.01)  # Use time.sleep for thread-based blocking

def worker(work_queue):
    while True:
        try:
            item = work_queue.get(timeout=0.01)  # Add a timeout to allow thread to exit
        except Empty:
            break
        else:
            print_number_sync(item)  # Call the synchronous function
            work_queue.task_done()

def threaded_pool(time_limit, num_threads):
    work_queue = Queue()
    work_queue.put(time_limit)  # Put the time limit as the work item
    threads = [
        Thread(target=worker, args=(work_queue,))
        for _ in range(num_threads)
    ]
    for thread in threads:
        thread.start()
    work_queue.join()
    for thread in threads:
        thread.join()

async def main():
    THREAD_POOL_SIZE = 12
    TIME_LIMIT = 3 * 60  # Set the time limit for the threaded operation

    print(f"Number of threads before start: {threading.active_count()}\n\n\n")

    start = datetime.now()
    threaded_pool(TIME_LIMIT, THREAD_POOL_SIZE)
    end = datetime.now()

    print("----------------")
    total_time = end - start
    print(f"Total Time (Threaded): {total_time.total_seconds():.2f}s")
    print(f"Number of Threads after running: {threading.active_count()}\n\n\n")

if __name__ == "__main__":
    asyncio.run(main())