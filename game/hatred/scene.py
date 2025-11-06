import pygame

import hatred.game_object

class Scene:
    def __init__(self, name: str, app) -> None:
        self.active = False
        self.name = name
        self.app = app

        self.game_objects: list[hatred.game_object.GameObject] = []

        # a default camera is necessary to keep track of world displacement
        # when it comes to rendering
        self.camera = hatred.game_object.GameObject("camera", self)

        self.app.add_scene(self)

    def append_game_object(self, obj: hatred.game_object.GameObject):
        self.game_objects.append(obj)

    def init(self) -> None:
        for obj in self.game_objects:
            obj.init()

    def update(self) -> None:
        for obj in self.game_objects:
            obj.update()

    def draw(self) -> None:
        for obj in self.game_objects:
            obj.draw()