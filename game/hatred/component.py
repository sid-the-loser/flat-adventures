import hatred.game_object

class Component:
    def __init__(self, name: str, game_object: hatred.game_object.GameObject) -> None:
        self.name: str = name
        self.game_object: hatred.game_object.GameObject = game_object

        self.game_object.append_component(self)
    
    def init(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass