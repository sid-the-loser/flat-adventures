import threading
import socket
import json
import random
import uuid

# TODO: might wanna switch to asyncio
# TODO: might wanna add a config setup

"""
{
    "<session_id>": 
    {
        "<uuid>": {
            "name": "<name>",
            "pos": [<x>, <y>]
        },
        ...
    },
    ...
}
"""

session_data = {}

conn_count = 0

running = True

session_id_size = 8
session_id_tokens = [chr(n) for n in list(range(65, 91)) + list(range(97, 123))]

lock = threading.Lock()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 6969))
server.listen()
server.settimeout(1.0)

def generate_session_id() -> str:
    id = ""

    for i in range(session_id_size):
        id += random.choice(session_id_tokens)

    if id in session_data:
        id = generate_session_id()
    
    return id

def console():
    global running

    print("Console thread started!")

    while running:
        ch = input()

        if ch == "stop":
            print("Stopping process started...")
            
            with lock:
                running = False

            print("Stopping everything...")

        if ch == "fstop":
            print("Force stopping everything...")
            with lock: 
                running = False
            
            server.close()

    print("Console thread stopped!")

def handler(conn: socket.socket, addr):
    global conn_count

    print(f"{addr} connected.")

    with lock:
        conn_count += 1

    """
    All done in json

    0 -> Connection type? (serve or join)
    1 -> Player data retrival
    """
    
    phase = 0

    is_host = False

    my_session = ""

    my_uuid = ""

    with conn:
        while running:
            try:
                raw_data = ""
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    else:
                        raw_data += data.decode()
                
                json_data = json.loads(raw_data)

                if phase == 1:
                    if my_session in session_data:
                        with lock:
                            if isinstance(json_data["pos"], list):
                                session_data[my_session][my_uuid]["pos"] = json_data["pos"]
                            else:
                                break

                            return_data = session_data[my_session]

                    else:
                        break

                elif phase == 0:
                    if json_data["type"] == "join":
                        if ("name" in json_data) and ("session_id" in json_data):
                            my_session = json_data["session_id"]

                            with lock:
                                if my_session in session_data:
                                    my_uuid = str(uuid.uuid4())
                                    session_data[my_session][my_uuid] = {
                                        "name": json_data["name"],
                                        "pos": [0, 0]
                                    }
                                else:
                                    break

                                return_data = {
                                    "uuid": my_uuid,
                                    "session_id": my_session,
                                    "exists": True
                                }

                                phase = 1

                        else:
                            break

                    elif json_data["type"] == "host":
                        if "name" in json_data:
                            my_session = generate_session_id()
                            my_uuid = str(uuid.uuid4())
                            is_host = True
                            with lock:
                                session_data[my_session] = {
                                    my_uuid: {
                                        "name": json_data["name"],
                                        "pos": [0, 0]
                                    }
                                }

                            return_data = {
                                "uuid": my_uuid,
                                "session_id": my_session,
                                "exists": True
                            }

                            phase = 1
                        else:
                            break

                conn.send(json.dumps(return_data).encode())
                    
            except:
                break

            if my_session != "":
                if is_host:
                    with lock:
                        del session_data[my_session]
                else:
                    with lock:
                        del session_data[my_session][my_uuid]

            conn.close()
            print(f"{addr} left.")

def listener():
    print("Listener thread started!")
    while running:
        try:
            conn, addr = server.accept()
            thread = threading.Thread(target=handler, args=(conn, addr))
            thread.start()
        except socket.timeout:
            continue

    print("Listener thread stopped!")

frontend = threading.Thread(target=console)
backend = threading.Thread(target=listener)

frontend.start()
backend.start()

frontend.join()
backend.join()