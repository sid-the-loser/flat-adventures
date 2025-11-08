import pygame

import hatred.math_plus
import hatred.component
import hatred.scene

class GameObject:
    def __init__(self, name: str, parent_scene) -> None:
        self.name: str = name
        self.scene: hatred.scene.Scene = parent_scene
        self.position = hatred.math_plus.Vector2()
        self.components: list[hatred.component.Component] = []

        self.scene.append_game_object(self)

    def append_component(self, component: hatred.component.Component):
        self.components.append(component)

    def init(self):
        for comp in self.components:
            comp.init()

    def update(self):
        for comp in self.components:
            comp.update()

    def draw(self):
        for comp in self.components:
            comp.draw()