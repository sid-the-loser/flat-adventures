import pygame
from random import randint
from typing import Any

from hatred.component import Component
from hatred.math_plus import Vector2, lerp
from hatred.game_details import WINDOW_SIZE

vec_half_window_size = Vector2(WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//2)

class RenderPawn(Component):
    def __init__(self, parent_game_object: Any, color: tuple[int, int, int], active: bool = True) -> None:
        super().__init__("RenderPawn", parent_game_object, active)

        self.color = color
        self.render_position = Vector2()

    def update(self):
        self.render_position = self.game_object.position - self.game_object.scene.world_render_origin

    def draw(self):
        window = self.game_object.scene.app.window

        pygame.draw.rect(window, self.color, (self.render_position.x, 
                                              self.render_position.y, 8, 8))
        
class PlayerMovement(Component):
    def __init__(self, parent_game_object: Any, active: bool = True) -> None:
        super().__init__("PlayerMovement", parent_game_object, active)

        self.walk_speed = 50
        self.input_direction = Vector2()
        self.friction = 1
        self.velocity = Vector2()

    def update(self):
        app = self.game_object.scene.app
        delta = app.delta_time

        self.input_direction = Vector2(
            int(app.input_is_pressed("right"))-int(app.input_is_pressed("left")),
            int(app.input_is_pressed("down"))-int(app.input_is_pressed("up"))
        )

        self.velocity.x = lerp(self.velocity.x, 
                               self.input_direction.x * self.walk_speed, 
                               self.friction * delta)
        self.velocity.y = lerp(self.velocity.y, 
                               self.input_direction.y * self.walk_speed, 
                               self.friction * delta)

        self.game_object.position.x += self.velocity.x
        self.game_object.position.y += self.velocity.y

        self.game_object.scene.world_render_origin = self.game_object.position - vec_half_window_size

class DummyMovement(Component):
    def __init__(self, parent_game_object: Any, active: bool = True) -> None:
        super().__init__("DummyMovement", parent_game_object, active)
        self.cell_size = 8

    def update(self):
        self.game_object.position.x += randint(-self.cell_size, self.cell_size)
        self.game_object.position.y += randint(-self.cell_size, self.cell_size)


class BackgroundColor(Component):
    def __init__(self, parent_game_object: Any, active: bool = True) -> None:
        super().__init__("BackgroundColor", parent_game_object, active)

    def update(self):
        app = self.game_object.scene.app
        if app.input_is_just_pressed("back"):
            app.switch_to_scene_index(1)

    def draw(self):
        self.game_object.scene.app.window.fill((0, 0, 0))