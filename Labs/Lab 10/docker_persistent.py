import docker
import time
import threading


client = docker.from_env()
print(client.containers.run("adminer"))
print(client.containers.run("mysql"))


containers = ["adminer", "mysql"]

def start_shutdown_check():

    while True:
        time.sleep(10)
        # check if containers are running every 10 secs
        for containerName in containers:
            container = client.containers.get(containerName)


            # restart at hour 1  
            if time.strftime("%H") == "01":
                container.restart()
                print(f"Container {containerName} restarted at {time.strftime('%H:%M:%S')}")


    


while True:
    time.sleep(10)










