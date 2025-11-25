import asyncio
import socket

# TODO: might wanna add a config setup

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 6969))