# https://docs.python.org/3/library/multiprocessing.html - multiprocessing man page

import time
from multiprocessing import Process, Queue, current_process, freeze_support, Manager, Lock

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def worker(input_q, highest_prime, lock, end_time):
  """Worker process to test numbers and update highest prime."""
  local_highest = 0
  while time.time() < end_time:  # Time-based stop condition
    try:
      num = input_q.get(timeout=0.1)  # Add timeout to avoid blocking
      if num is None:  # Termination signal
        break
      if is_prime(num):
        local_highest = max(local_highest, num)
        with lock:
          highest_prime.value = max(highest_prime.value, local_highest)
    except Queue.Empty:  # Handle timeout
      pass

def main(num_processes, run_time):
  """Main function to manage processes and calculate execution time."""
  manager = Manager()
  input_q = Queue()
  highest_prime = manager.Value('i', 0)
  lock = Lock()

  processes = []
  end_time = time.time() + run_time  # Calculate end time
  for _ in range(num_processes):
    p = Process(target=worker, args=(input_q, highest_prime, lock, end_time))
    processes.append(p)
    p.start()

  start_time = time.time()
  num = 0
  while time.time() < end_time:  # Time-based loop
    input_q.put(num)
    num += 1

  # Send termination signals (optional, workers will stop due to time condition) - chatgpted
  for _ in range(num_processes):
    input_q.put(None)

  for p in processes:
    p.join()

  end_time = time.time()  # Update end time for accurate calculation

  print(f"Highest prime found: {highest_prime.value}")
  print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
  freeze_support()
  num_processes = 12  # Adjust the number of processes
  run_time = 3 * 60   # Adjust the run time in seconds
  main(num_processes, run_time)



