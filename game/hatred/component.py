import hatred.game_object
import hatred.app

class Component:
    def __init__(self, name: str, parent_game_object, active: bool = True) -> None:
        self.name: str = name
        self.game_object: hatred.game_object.GameObject = parent_game_object
        self.active = active

        self.game_object.append_component(self)
    
    def init(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

class GlobalComponent:
    def __init__(self, name: str, parent_app) -> None:
        self.name: str = name
        self.app: hatred.app.App = parent_app

        self.app.add_global_component(self)
    
    def init(self) -> None:
        pass

    def early_update(self) -> None:
        pass

    def late_update(self) -> None:
        pass

    def early_draw(self) -> None:
        pass

    def late_draw(self) -> None:
        pass