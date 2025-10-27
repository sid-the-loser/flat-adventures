import yaml
import os
from copy import deepcopy

# Dealing with configuration files

CONFIG_FILE_LOCATION: str = "./config.yaml"

default_config: dict = {
    "server-details": {
        "ip": "localhost",
        "port": 6969
    }
}

config: dict = deepcopy(default_config)

config_exists: bool = os.path.isfile(CONFIG_FILE_LOCATION)

config_updated: bool = False

if not config_exists:
    with open(CONFIG_FILE_LOCATION, "w") as f:
        yaml.safe_dump(config, f)
        config_updated = True

elif config_exists:
    with open(CONFIG_FILE_LOCATION) as f:
        config = yaml.safe_load(f)

    for key in default_config:
        if key not in config:
            config[key] = default_config[key]
        elif not isinstance(config[key], type(default_config[key])):
            config[key] = default_config[key]