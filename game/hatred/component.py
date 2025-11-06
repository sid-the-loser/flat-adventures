import pygame

class Component:
    def __init__(self, name) -> None:
        self.name: str = name
    
    def init(self):
        pass

    def update(self, delta: float):
        pass

    def draw(self, surface: pygame.Surface):
        pass