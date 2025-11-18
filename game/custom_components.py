import pygame

from hatred.game_details import WINDOW_SIZE
from hatred.game_object import GameObject
from hatred.component import Component
from hatred.math_plus import Vector2, lerp

class PlayerControls(Component):
    def __init__(self, parent_game_object) -> None:
        super().__init__("PlayerControls", parent_game_object)

        self.movement_dirction = Vector2()
        self.velocity = Vector2()
    
    def init(self):
        self.movement_dirction *= 0
        self.velocity *= 0

    def update(self):
        events = self.game_object.scene.app.events

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.game_object.position.x -= 100
                    print("yes")
                elif event.key == pygame.K_d:
                    self.game_object.position.x += 100
                    print("no")

            if event.type == pygame.KEYUP:
                pass

class DrawPlayer(Component):
    def __init__(self, parent_game_object) -> None:
        super().__init__("DrawRect", parent_game_object)
        
    def draw(self):
        return super().draw()