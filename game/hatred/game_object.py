import hatred.math_plus
import hatred.component
import hatred.scene

class GameObject:
    def __init__(self, name: str, parent_scene, active: bool = True) -> None:
        self.name: str = name
        self.scene: hatred.scene.Scene = parent_scene
        self.active = active

        self.position = hatred.math_plus.Vector2()
        self.components: list[hatred.component.Component] = []

        self.scene.append_game_object(self)

    def append_component(self, component: hatred.component.Component) -> None:
        self.components.append(component)

    def find_component_by_name(self, name: str) -> hatred.component.Component | None:
        for i in range(len(self.components)):
            if self.components[i].name == name:
                return self.components[i]
        else:
            return None
        
    def find_component_index_by_name(self, name: str) -> int:
        for i in range(len(self.components)):
            if self.components[i].name == name:
                return i
        else:
            return -1

    def init(self) -> None:
        for comp in self.components:
            comp.init()

    def update(self) -> None:
        for comp in self.components:
            comp.update()

    def draw(self) -> None:
        for comp in self.components:
            comp.draw()