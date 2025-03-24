import time
from multiprocessing import Process, Queue, current_process, freeze_support

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def worker(input_q, output_q, highest_prime, lock):
  """Worker process to test numbers and update highest prime."""
  local_highest = 0
  while True:
    num = input_q.get()
    if num is None:  # Termination signal
      break
    
    if is_prime(num):
      print
      local_highest = max(local_highest, num)

      with lock:
        highest_prime.value = max(highest_prime.value, local_highest)

def main(num_processes, range_end):
    """Main function to manage processes and calculate execution time."""
    manager = Manager()
    input_q = Queue()
    output_q = Queue()
    highest_prime = manager.Value('i', 0)  # Shared highest prime
    lock = Lock()  # Lock to protect shared variable

    processes = []
    for _ in range(num_processes):
        p = Process(target=worker, args=(input_q, output_q, highest_prime, lock))
        processes.append(p)
        p.start()

    start_time = time.time()
    for num in range(0, range_end):
        input_q.put(num)

    # Send termination signals to worker processes
    for _ in range(num_processes):
        input_q.put(None)

    for p in processes:
        p.join()

    end_time = time.time()

    print(f"Highest prime found: {highest_prime.value}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    freeze_support()
    num_processes = 4  # Adjust the number of processes
    range_end = 10000  # Adjust the range of numbers to test
    main(num_processes, range_end)