import logging
import random
import time
from datetime import datetime




# quizkly makes a sample logfile dseired for the parser to read from


options = ["INFO", "WARNING", "ERROR", "CRITICAL"]
possible_messages = [ " System failure", "Database corruption",
    "Disk failure detected", "Database corruption"]

file_path_base = "logGLfolder\\log"
file_path_postfix_core = "_core"
file_path_postfix_utils = "_utils"
file_path_second_postfix = "_db"

postfix_group = [file_path_postfix_core, file_path_postfix_utils,0]

second_postfix_group = [file_path_second_postfix,0]


file_path_extension = ".log"




now = datetime.now()

def getCurrentTime():
    return now.strftime("%Y-%m-%d %H:%M:%S")

def getRandomLogLevel():
    return random.choice(options)

def getRandomMessage():
    return random.choice(possible_messages)



def logGenerator():
    # Generated log messages - not the log handler way wanted but you said this was okay when asked in person :)
    for i in range(100):
        log_level = getRandomLogLevel()
        message = getRandomMessage()

        postfix = random.choice(postfix_group)
        second_postfix = random.choice(second_postfix_group)


        

        if postfix == 0:
            file_path = file_path_base + file_path_extension

            log_message = f"{getCurrentTime()} | {file_path} | {log_level} | {message}\n"

            with open(file_path, "a") as file:
                    file.write(log_message)
        else:
            if second_postfix == 0:
                file_path = file_path_base + postfix + file_path_extension


                log_message = f"{getCurrentTime()} | {file_path} | {log_level} | {message}\n"
            

                # can be done recursively - split by the underscore remove the last item and recombine into a string
                with open(file_path, "a") as file:
                    file.write(log_message)

                file_path = file_path_base + file_path_extension

                with open(file_path, "a") as file:
                    file.write(log_message)




            else:
                file_path = file_path_base + postfix + second_postfix + file_path_extension

                log_message = f"{getCurrentTime()} | {file_path} | {log_level} | {message}\n"
            
                with open(file_path, "a") as file:
                    file.write(log_message)

                file_path = file_path_base + postfix + file_path_extension

                with open(file_path, "a") as file:
                    file.write(log_message)

                file_path = file_path_base  + file_path_extension

                with open(file_path, "a") as file:
                    file.write(log_message)





    


  



    



  

