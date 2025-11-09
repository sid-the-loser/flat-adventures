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
                pass

            if event.type == pygame.KEYUP:
                pass

class DrawPlayer(Component):
    def __init__(self, parent_game_object) -> None:
        super().__init__("DrawRect", parent_game_object)
        self.render_position: Vector2 = Vector2()
        self.rect_size = Vector2(8, 16)

    def init(self):
        self.game_object.scene.world_render_origin.set(
            self.game_object.position.x - (self.rect_size.x // 2),
            self.game_object.position.y - (self.rect_size.y // 2)
        )

        self.render_position.set(
            self.game_object.scene.world_render_origin.x - WINDOW_SIZE[0],
            self.game_object.scene.world_render_origin.y - WINDOW_SIZE[1]
        )

    def draw(self):
        pygame.draw.rect(self.game_object.scene.app.window, (255, 0, 0), 
                         (self.render_position.x, self.render_position.x, 
                          self.rect_size.x, self.rect_size.y))