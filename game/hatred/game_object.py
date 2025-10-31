import pygame

import hatred.math_plus

class GameObject:
    def __init__(self, name) -> None:
        self.name: str = name
        self.position = hatred.math_plus.Vector2()

    def init(self):
        pass

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        pass