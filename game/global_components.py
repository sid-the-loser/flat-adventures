import pygame
import yaml
import os
from copy import deepcopy

from hatred.component import GlobalComponent
from hatred.game_details import IS_BUILD

default_config = {
    "proxy_details": {
        "ip": "localhost",
        "port": "6969"
    }
}

class ConfigForP2P(GlobalComponent):
    def __init__(self, parent_app, path: str) -> None:
        super().__init__("ConfigForP2P", parent_app)
        self.path: str = path
        self.config: dict = {}
        
        self.load_config()

    def load_config(self):
        if os.path.isfile(self.path):
            with open(self.path) as f:
                self.config = yaml.safe_load(f)

        else:
            self.config = deepcopy(default_config)
            self.save_config()

    def save_config(self):
        with open(self.path) as f:
            yaml.safe_dump(self.config, f)


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