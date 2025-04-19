import docker

client = docker.from_env()

print("Docker version:", client.version()['Version'])



def show_container_ip(container_name):
    container = client.containers.get(container_name)
    networks = container.attrs['NetworkSettings']['Networks']
    
    for net_name, net_data in networks.items():
        print(f"{container_name} in network '{net_name}' has IP: {net_data['IPAddress']}")


show_container_ip("adminer")
show_container_ip("mysql")