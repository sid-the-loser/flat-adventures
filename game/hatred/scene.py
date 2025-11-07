import pygame

import hatred.game_object
import hatred.app

class Scene:
    def __init__(self, name: str, app: hatred.app.App) -> None:
        self.active = False
        self.name = name
        self.app: hatred.app.App = app

        self.game_objects: list[hatred.game_object.GameObject] = []

        # a default camera is necessary to keep track of world displacement
        # when it comes to rendering
        self.camera = hatred.game_object.GameObject("camera", self)

        self.app.add_scene(self)

    def append_game_object(self, obj: hatred.game_object.GameObject) -> None:
        self.game_objects.append(obj)

    def remove_game_object(self, game_object: hatred.game_object.GameObject) -> None:
        self.game_objects.remove(game_object)

    def remove_game_object_by_name(self, name: str) -> None:
        potential_index = self.find_game_object_index_by_name(name)

        if potential_index >= 0:
            pass

    def find_game_object_by_name(self, name: str) -> hatred.game_object.GameObject | None:
        for i in range(len(self.game_objects)):
            if self.game_objects[i].name == name:
                return self.game_objects[i]
        else:
            return None
        
    def find_game_object_index_by_name(self, name: str) -> int:
        for i in range(len(self.game_objects)):
            if self.game_objects[i].name == name:
                return i
        else:
            return -1

    def init(self) -> None:
        for obj in self.game_objects:
            obj.init()

    def update(self) -> None:
        for obj in self.game_objects:
            obj.update()

    def draw(self) -> None:
        for obj in self.game_objects:
            obj.draw()