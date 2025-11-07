import hatred.game_object

class Component:
    def __init__(self, name: str, game_object: hatred.game_object.GameObject) -> None:
        self.name: str = name
    
    def init(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass