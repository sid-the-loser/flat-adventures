from typing import Any

import hatred.game_object
import hatred.app
import hatred.math_plus

class Scene:
    def __init__(self, name: str, parent_app: Any) -> None:
        self.active = False
        self.name = name
        self.app: hatred.app.App = parent_app

        self.game_objects: list[hatred.game_object.GameObject] = []
        self.render_sorted_game_objects: list[hatred.game_object.GameObject] = []

        self.world_render_origin = hatred.math_plus.Vector2() # worlds kinda like a camera

        self.app.add_scene(self)

    def append_game_object(self, obj: hatred.game_object.GameObject) -> None:
        self.game_objects.append(obj)
        self.add_render_sort(obj)

    def remove_game_object(self, game_object: hatred.game_object.GameObject) -> None:
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)
        else:
            raise NoSuchGameObjectFound(f"GameObject \"{game_object.name}\" not found in this scene \"{self.name}\"!")

    def remove_game_object_by_name(self, name: str) -> None:
        potential_index = self.find_game_object_index_by_name(name)

        if potential_index >= 0:
            self.game_objects.pop(potential_index)
        else:
            raise NoSuchGameObjectFound(f"GameObject with \"{name}\" not found in this scene \"{self.name}\"!")

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
            if obj.active:
                obj.init()

    def update(self) -> None:
        for obj in self.game_objects:
            if obj.active:
                obj.update()

    def draw(self) -> None:
        for obj in self.render_sorted_game_objects:
            if obj.active:
                obj.draw()

    def add_render_sort(self, new_obj: hatred.game_object.GameObject) -> None:
        self.render_sorted_game_objects.append(new_obj)
        self.update_render_sort()

    def update_render_sort(self):
        self.render_sorted_game_objects = sorted(self.render_sorted_game_objects, 
                                                 key=lambda go: go.layer)

class NoSuchGameObjectFound(Exception):
    pass