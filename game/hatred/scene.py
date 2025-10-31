import pygame

import hatred.game_object

class Scene:
    def __init__(self, name: str) -> None:
        self.active = False
        self.name = name

        self.game_objects: list[hatred.game_object.GameObject] = []

        # a default camera is necessary to keep track of world displacement
        # when it comes to rendering
        self.camera = hatred.game_object.GameObject("camera")

    def init(self) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass