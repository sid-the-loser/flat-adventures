import pygame

import hatred.math_plus
import hatred.component
import hatred.scene

class GameObject:
    def __init__(self, name: str, scene: hatred.scene.Scene) -> None:
        self.name: str = name
        self.scene: hatred.scene.Scene = scene
        self.position = hatred.math_plus.Vector2()
        self.components: list[hatred.component.Component] = []

    def init(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass