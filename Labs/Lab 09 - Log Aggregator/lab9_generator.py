import logging
import random
import time
from datetime import datetime


options = ["INFO", "WARNING", "ERROR", "CRITICAL"]
possible_messages = [ " System failure", "Database corruption",
    "Disk failure detected", "Database corruption"]

now = datetime.now()

def getCurrentTime():
    return now.strftime("%Y-%m-%d %H:%M:%S")

def getRandomLogLevel():
    return random.choice(options)

def getRandomMessage():
    return random.choice(possible_messages)





file_path = "logGL.log"




for i in range(100):
    log_level = getRandomLogLevel()
    message = getRandomMessage()
    log_message = f"{getCurrentTime()} | {log_level} | {message} \n"
    print(log_message)
    with open(file_path, "a") as file:
        file.write(log_message)



  

