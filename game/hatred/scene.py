import pygame

class Scene:
    def __init__(self, name: str) -> None:
        self.active = False
        self.name = name

    def init(self) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass