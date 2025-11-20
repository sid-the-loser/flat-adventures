import pygame
import os

from hatred.component import Component
from hatred.math_plus import lerp

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

ASSETS_PATH = os.path.join(BASE_PATH, "assets/")

FONTS_PATH = os.path.join(ASSETS_PATH, "fonts/Tiny5-Regular.ttf")

class TitleLabel(Component):
    def __init__(self, parent_game_object, active: bool = True) -> None:
        super().__init__("TitleLabel", parent_game_object, active)
        self.title_font = pygame.font.Font(FONTS_PATH, 72)

        self.title_img = self.title_font.render("Flat Adventures", True, 
                                                (255, 255, 255))
        self.title_rect = self.title_img.get_rect()

        self.title_rect.x = 50
        self.title_rect.y = 250

        self.animation_speed_x = self.title_rect.x / self.title_rect.y

        self.title_triggered_flag = False

    def update(self):
        global title_triggered_flag

        delta = self.game_object.scene.app.delta_time

        if not self.title_triggered_flag:
            for event in self.game_object.scene.app.events:
                if event.type == pygame.KEYDOWN:
                    self.title_triggered_flag = True

        else:
            if self.title_rect.x != 0 or self.title_rect.y != 0:
                self.title_rect.x = lerp(self.title_rect.x, 0, 
                                         delta * self.animation_speed_x)
                self.title_rect.y = lerp(self.title_rect.y, 0, delta)

    def draw(self):
        self.game_object.scene.app.window.blit(self.title_img, self.title_rect)