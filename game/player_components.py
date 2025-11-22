import pygame

from hatred.game_details import WINDOW_SIZE
from hatred.component import Component
from hatred.math_plus import Vector2, lerp

class PlayerControls(Component):
    def __init__(self, parent_game_object) -> None:
        super().__init__("PlayerControls", parent_game_object)

        self.movement_speed = 10
        self.friction = 5

        self.input_direction: list[int] = [0, 0, 0, 0]
        self.movement_direction = Vector2()
        self.velocity = Vector2()
    
    def init(self) -> None:
        self.movement_direction *= 0
        self.velocity *= 0

    def update(self) -> None:
        events = self.game_object.scene.app.events
        delta = self.game_object.scene.app.delta_time

        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.input_direction[0] = 0

                if event.key == pygame.K_d:
                    self.input_direction[1] = 0

                if event.key == pygame.K_w:
                    self.input_direction[2] = 0

                if event.key == pygame.K_s:
                    self.input_direction[3] = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.input_direction[0] = 1

                if event.key == pygame.K_d:
                    self.input_direction[1] = 1

                if event.key == pygame.K_w:
                    self.input_direction[2] = 1

                if event.key == pygame.K_s:
                    self.input_direction[3] = 1

        self.movement_direction.set(self.input_direction[1]-self.input_direction[0],
                                    self.input_direction[3]-self.input_direction[2])

        self.velocity.set(lerp(self.velocity.x, 
                               self.movement_direction.x * self.movement_speed, 
                               delta * self.friction),
                          lerp(self.velocity.y, 
                               self.movement_direction.y * self.movement_speed, 
                               delta * self.friction))
        
        self.game_object.position += self.velocity

class DrawPlayer(Component):
    def __init__(self, parent_game_object) -> None:
        super().__init__("DrawPlayer", parent_game_object)
        self.cam_offset = (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)

        self.cam_speed = 10

    def init(self) -> None:
        self.game_object.scene.world_render_origin.set(
                self.cam_offset[0] - self.game_object.position.x, # displacement of 300 on both x and y
                self.cam_offset[1] - self.game_object.position.y
            )

    def update(self) -> None:
        wro = self.game_object.scene.world_render_origin
        dt = self.game_object.scene.app.delta_time

        self.game_object.scene.world_render_origin.set(
            lerp(wro.x, self.cam_offset[0] - self.game_object.position.x, 
                 dt * self.cam_speed), # displacement of 300 on both x and y
            lerp(wro.y, self.cam_offset[1] - self.game_object.position.y, 
                 dt * self.cam_speed)
        )
        
    def draw(self) -> None:
        wro = self.game_object.scene.world_render_origin

        pygame.draw.rect(self.game_object.scene.app.window, (255, 0, 0), 
                         (self.game_object.position.x + wro.x, 
                          self.game_object.position.y + wro.y, 8, 8))
        
class DrawDummy(Component):
    def __init__(self, parent_game_object) -> None:
        super().__init__("DrawDummy", parent_game_object)
        
    def draw(self) -> None:
        wro = self.game_object.scene.world_render_origin

        pygame.draw.rect(self.game_object.scene.app.window, (0, 255, 0), 
                         (self.game_object.position.x + wro.x, 
                          self.game_object.position.y + wro.y, 8, 8))
