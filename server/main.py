import socket
import yaml
import os
from copy import deepcopy

# Dealing with configuration files

default_config = {
    "config-file-details": {
        "version": "1.0"
    },
    "server-details": {
        "ip": "localhost",
        "port": 6969
    }
}

config = deepcopy(default_config)

if not os.path.isfile("./config.yaml"):
    pass