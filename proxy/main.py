import socket
import yaml
import os

default_config = {
    "ip": "127.0.0.1",
    "port": 65432
}

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                           "config.yaml")