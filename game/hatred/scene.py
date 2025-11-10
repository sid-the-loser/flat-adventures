from copy import deepcopy

import hatred.game_object
import hatred.app
import hatred.math_plus

class Scene:
    def __init__(self, name: str, parent_app) -> None:
        self.active = False
        self.name = name
        self.app: hatred.app.App = parent_app

        self.game_objects: list[hatred.game_object.GameObject] = []
        self.render_sorted_game_objects: list[hatred.game_object.GameObject] = []

        self.world_render_origin = hatred.math_plus.Vector2() # worlds kinda like a camera

        self.app.add_scene(self)

    def append_game_object(self, obj: hatred.game_object.GameObject) -> None:
        self.game_objects.append(obj)
        self.render_sort(obj)

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

    def render_sort(self, new_obj: hatred.game_object.GameObject):
        if len(self.render_sorted_game_objects):
            pass # work on this