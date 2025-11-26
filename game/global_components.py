import pygame
import yaml
import os
from copy import deepcopy
import socket
import threading
import json

from hatred.component import GlobalComponent
from hatred.game_details import IS_BUILD

default_config = {
    "proxy_details": {
        "ip": "localhost",
        "port": 6969
    },
    "player_details": {
        "name": "John"
    }
}

lock = threading.Lock()

class ServerModel(GlobalComponent):
    def __init__(self, parent_app, path: str) -> None:
        super().__init__("ServerModel", parent_app)
        self.path: str = path
        self.config: dict = {}

        self.world_data = {}

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.is_connected = False
        
        self.load_config()

        self.client_name = self.config["player_details"]["name"]
        self.position = [0.0, 0.0]
        self.ip = self.config["proxy_details"]["ip"]
        self.port = self.config["proxy_details"]["port"]

        self.my_thread = threading.Thread(target=self.main)
        self.my_thread.start()

    def load_config(self):
        if os.path.isfile(self.path):
            with open(self.path) as f:
                self.config = yaml.safe_load(f)

        else:
            self.config = deepcopy(default_config)
            self.save_config()

    def save_config(self):
        with open(self.path, "w") as f:
            yaml.safe_dump(self.config, f)

    def connect(self):
        self.client.connect((self.ip, self.port))
        self.is_connected = True

    def main(self):
        while self.app.app_running:
            if self.is_connected:
                self.client.send(json.dumps({
                    # TODO: work here!
                }).encode())
                raw_data = ""
                while True:
                    data = self.client.recv(1024)
                    if not data:
                        break
                    else:
                        raw_data += data.decode()

                json_data = json.loads(raw_data)



class DebugKeyLogic(GlobalComponent):
    def __init__(self, parent_app) -> None:
        super().__init__("DebugEvents", parent_app)
        self.show_debug_overlay = False

        # NOTE: Mac works weirdly with function keys so, we kinda need this
        self.debug_alt_key_flag = False 

    def early_update(self) -> None:
        events = self.app.events

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL:
                    self.debug_alt_key_flag = True

                if event.key == pygame.K_F2:
                    pass # TODO: screenshot functionality

                if event.key == pygame.K_F3:
                    self.show_debug_overlay = not self.show_debug_overlay

                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
                    # NOTE: This function works really badly with some display drivers is you are using pygame 1

                if event.key == pygame.K_ESCAPE:
                    if not IS_BUILD: # TODO: Removed later to support pause menu
                        if self.app.current_scene.name != "Singleplayer":
                            self.app.app_running = False
                        else:
                            self.app.switch_to_scene("MainMenu")

                if self.debug_alt_key_flag:
                    if event.key == pygame.K_p:
                        pass # TODO: screenshot functionality

                    if event.key == pygame.K_o:
                        self.show_debug_overlay = not self.show_debug_overlay
                    
                    if event.key == pygame.K_l:
                        pygame.display.toggle_fullscreen()
                        # NOTE: This function works really badly with some display drivers is you are using pygame 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LCTRL:
                    self.debug_alt_key_flag = False