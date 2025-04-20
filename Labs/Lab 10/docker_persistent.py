import docker
import time
import threading
import logging


client = docker.from_env()
containers = ["adminer", "mysql"]

# taken from notes
logger = logging.getLogger()

logger.setLevel(logging.INFO) # set the logging level to INFO

formatter = logging.Formatter(
    fmt=(
        "%(asctime)s | %(levelname)s | "
        "%(message)s"
    )
)
handler = logging.handlers.TimedRotatingFileHandler(
    filename="formatedLog.log",
    when="D",
    backupCount=3,
)
# create a file handler that logs to a file
logger.addHandler(
    logging.handlers.TimedRotatingFileHandler(
        filename="archived_log.log", #file name
        when="D", #rolls the log every day
        backupCount=3, # only keep 3 days worth of file backups
    )
)

# used https://docker-py.readthedocs.io/en/stable/containers.html

def start_shutdown_check():

    while True:
        time.sleep(10)
        # check if containers are running every 10 secs
        for containerName in containers:
            container = client.containers.get(containerName)

            if container.status != "running":
                # if not running, start the container
                container.start()
                print(f"Container {containerName} started at {time.strftime('%H:%M:%S')}")
            # restart at hour 1  
            if time.strftime("%H") == "01":
                container.restart()
                print(f"Container {containerName} restarted at {time.strftime('%H:%M:%S')}")


    

if __name__ == "__main__":
    shutdown_thread = threading.Thread(target=start_shutdown_check)
    shutdown_thread.start()

    # wanted to make another thread that would open the log stream and print it

    










