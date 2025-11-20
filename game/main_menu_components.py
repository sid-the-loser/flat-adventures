import pygame
import os

from hatred.component import Component
from hatred.math_plus import lerp

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

ASSETS_PATH = os.path.join(BASE_PATH, "assets/")

title_triggered_flag = False

FONTS_PATH = os.path.join(ASSETS_PATH, "fonts/Tiny5-Regular.ttf")

print(FONTS_PATH)

TITLE_FONT = pygame.font.Font(FONTS_PATH, 72)

class TitleLabel(Component):
    def __init__(self, parent_game_object, active: bool = True) -> None:
        super().__init__("TitleLabel", parent_game_object, active)
        self.img = TITLE_FONT.render("Flat Adventures", True, (255, 255, 255))
        self.rect = self.img.get_rect()
        self.rect.x = 50
        self.rect.y = 250

    def update(self):
        global title_triggered_flag

        delta = self.game_object.scene.app.delta_time

        if not title_triggered_flag:
            for event in self.game_object.scene.app.events:
                if event.type == pygame.KEYDOWN:
                    title_triggered_flag = True

        else:
            if self.rect.x != 0 or self.rect.y != 0:
                self.rect.x = lerp(self.rect.x, 0, delta)
                self.rect.y = lerp(self.rect.y, 0, delta)

    def draw(self):
        self.game_object.scene.app.window.blit(self.img, self.rect)