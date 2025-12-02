import pygame
import os
from typing import Any

from hatred.component import Component
from hatred.game_details import WINDOW_SIZE, ASSETS_PATH

window_center = [WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2]

font_path: str = os.path.join(ASSETS_PATH, "fonts/Tiny5-Regular.ttf")

h1_font = pygame.font.SysFont(None, 72)
h2_font = pygame.font.SysFont(None, 32)

class Title(Component):
    def __init__(self, parent_game_object: Any, active: bool = True) -> None:
        super().__init__("Title", parent_game_object, active)

        self.text_surface = h1_font.render("Flat Adventures", True, 
                                           (255, 255,255))
        self.text_rect = self.text_surface.get_rect(center=window_center)

    def draw(self):
        window = self.game_object.scene.app.window

        window.blit(self.text_surface, self.text_rect)

class Background(Component):
    def __init__(self, parent_game_object: Any, active: bool = True) -> None:
        super().__init__("Background", parent_game_object, active)

    def draw(self):
        window = self.game_object.scene.app.window

        window.fill((0, 0, 0))

class SubTitle(Component):
    def __init__(self, parent_game_object: Any, active: bool = True) -> None:
        super().__init__('SubTitle', parent_game_object, active)

        self.text_surface = h2_font.render("Press space key to continue!", True,
                                           (255, 255, 0))
        self.text_rect = self.text_surface.get_rect(center=(window_center[0], window_center[1]+(36+16)))

        self.app = self.game_object.scene.app

    def update(self):
        if self.app.input_is_just_pressed("main_menu"):
            self.app.switch_to_scene_index(2)

    def draw(self):
        window = self.app.window

        window.blit(self.text_surface, self.text_rect)
