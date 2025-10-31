import socket
import threading
import yaml
import os
from copy import deepcopy

default_config = {
    "ip": "127.0.0.1",
    "port": 8080
}

local_config = {}

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                           "config.yaml")

if os.path.isfile(CONFIG_PATH):
    with open(CONFIG_PATH) as f:
        local_config = yaml.safe_load(f)

    patch_config_flag = False

    for key in default_config:
        if key not in local_config:
            local_config[key] = default_config[key]
            patch_config_flag = True

        elif not isinstance(local_config[key], type(default_config[key])):
            local_config[key] = default_config[key]
            patch_config_flag = True

    
    if patch_config_flag:
        with open(CONFIG_PATH, "w") as f:
            yaml.dump(local_config, f)

else:
    with open(CONFIG_PATH, "w") as f:
        yaml.dump(default_config, f)

    local_config = deepcopy(default_config)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((local_config["ip"], local_config["port"]))
server.listen()

print(f"Server is not listening on {local_config['ip']}:{local_config['port']}")

running = True
connection_count = 0

lock = threading.Lock()

def console():
    global running

    print("Server console thread started!")
    while running:
        command = input("")

        if command == "stop":
            with lock:
                running = False

        elif command == "count":
            print(f"Connection count: {connection_count}")

    print("Server console thread stopped!")

def handler(conn: socket.socket, addr):
    global connection_count

    print(f"{addr} connected.")

    with lock:
        connection_count += 1

    with conn:
        while running:
            data = conn.recv(1024)
            if not data:
                break
            print(f"{addr}: {data.decode()}")
            conn.sendall(data)

    with lock:
        connection_count -= 1

    print(f"{addr} disconnected.")

def main():
    print("Server main thread started!")

    while running:
        try:
            server.settimeout(1.0)
            conn, addr = server.accept()
            thread = threading.Thread(target=handler, args=(conn, addr))
            thread.start()
        except socket.timeout:
            continue

    print("Server main thread stopped!")

frontend = threading.Thread(target=console)
backend = threading.Thread(target=main)

frontend.start()
backend.start()

frontend.join()
backend.join()
