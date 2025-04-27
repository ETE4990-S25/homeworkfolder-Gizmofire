import logging
import random
import time
from datetime import datetime


dictionary = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}



def new_line_reader(log_file_path):
  try:
    with open(log_file_path, 'r') as file_:
      file_.seek(0, 2)

      while True:
        line = file_.readline()
        if not line:
          time.sleep(0.1)  # Wait briefly if no new lines
          continue
        yield line
  except FileNotFoundError:
    print(f"Error: Log file not found at {log_file_path}")
  except Exception as e:
    print(f"An error occurred: {e}")



# file_path = "logGL.log"
# with open(file_path, "r") as file:
#   for line in file:
    
#     print(line.split("|"))
    
#     dictionary.add(line.split("|"))
# print(dictionary)

def logParser(log_file_path):

  if not log_file_path:
    log_file_path = "logGL.log"
  log_generator = new_line_reader(log_file_path)
  print(f"Monitoring log file: {log_file_path}")

  try:
    for line in log_generator:
        print(f"New log entry: {line.strip()}")
        items = line.split("|")
        # format of data, [time, file_path, log_level, message]
        print(items[3])
  except KeyboardInterrupt:
    print("\nMonitoring stopped.")




if __name__ == "__main__":
  log_file_path = "logGL.log"
  logParser(log_file_path)

  







  

