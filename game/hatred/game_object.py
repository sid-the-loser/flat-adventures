import pygame

import hatred.math_plus
import hatred.component

class GameObject:
    def __init__(self, name: str, scene) -> None:
        self.name: str = name
        self.scene = scene
        self.position = hatred.math_plus.Vector2()
        self.components: list[hatred.component.Component] = []

        self.scene.append_game_object(self)

    def init(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass