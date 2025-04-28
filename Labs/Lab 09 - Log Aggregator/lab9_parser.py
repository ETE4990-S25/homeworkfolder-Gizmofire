import logging
import random
import time
from datetime import datetime



# pretty much does 2b and 3a 
# creates a thread that reads the log as its being written to 
# at the end pritns the summary of the log file for all levels of logging including critical


dictionary = {"INFO": {}, "WARNING": {}, "ERROR": {}, "CRITICAL": {}}



def new_line_reader(log_file_path):
  try:
    with open(log_file_path, 'r') as file_:
      file_.seek(0, 2)

      while True:
        line = file_.readline()
        if not line:
          time.sleep(0.001)  # Wait briefly if no new lines
          continue
        yield line
  except FileNotFoundError:
    print(f"Error: Log file not found at {log_file_path}")
  except Exception as e:
    print(f"An error occurred: {e}")

# added this 
def exitTimer():
  # Exit timer for the program
  print("Exiting in 10 seconds...")
  time.sleep(10)
  print("Exiting now.")
  exit(0)



def logParser(log_file_path, data_dict):

  if not log_file_path:
    log_file_path = "logGL.log"
  log_generator = new_line_reader(log_file_path)
  print(f"Monitoring log file: {log_file_path}")

  try:
    for line in log_generator:
      # print(f"New log entry: {line.strip()}")
      items = line.split("|")
      # format of data, [time, file_path, log_level, message]
      # print(items[2])

      if (items[2].strip() == "CRITICAL"):
        print("Critical log entry detected!\n")
        print(f"Time: {items[0]} CRITICAL Found at {items[1]} with message: {items[3]}")



      if items[2].strip() in data_dict:
        if 'count' not in data_dict[items[2].strip()]:
          data_dict[items[2].strip()]['count'] = 0
          # print(f"Updated dictionary: {data_dict}")

        data_dict[items[2].strip()]['count'] += 1
        # print(f"Updated dictionary: {data_dict}")
    
      
        if items[3].strip() in data_dict[items[2].strip()]:
          data_dict[items[2].strip()][items[3].strip()] += 1
        else:
          data_dict[items[2].strip()][items[3].strip()] = 1
          # print(f"Updated dictionary: {data_dict}")

  except KeyboardInterrupt:
    print("\nMonitoring stopped.")




if __name__ == "__main__":
  log_file_path = "logGL.log"
  logParser(log_file_path, dictionary)
  exitTimer()

  







  

