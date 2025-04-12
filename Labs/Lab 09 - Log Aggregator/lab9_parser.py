import logging
import random
import time
from datetime import datetime


dictionary = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}







file_path = "logGL.log"
with open(file_path, "r") as file:
  for line in file:
    
    print(line.split("|"))
    
    dictionary.add(line.split("|"))
print(dictionary)






  

