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
                elif event.key == pygame.K_d:
                    self.game_object.position.x += 100

                if event.key == pygame.K_w:
                    self.game_object.position.y -= 100
                elif event.key == pygame.K_s:
                    self.game_object.position.y += 100

            if event.type == pygame.KEYUP:
                pass

class DrawPlayer(Component):
    def __init__(self, parent_game_object) -> None:
        super().__init__("DrawPlayer", parent_game_object)

    def init(self):
        self.game_object.scene.world_render_origin = Vector2(
                300 - self.game_object.position.x, # displacement of 300 on both x and y
                300 - self.game_object.position.y
            )

    def update(self):
        wro = self.game_object.scene.world_render_origin
        dt = self.game_object.scene.app.delta_time

        self.game_object.scene.world_render_origin = Vector2(
            lerp(wro.x, 300 - self.game_object.position.x, dt), # displacement of 300 on both x and y
            lerp(wro.y, 300 - self.game_object.position.y, dt)
        )
        
    def draw(self):
        wro = self.game_object.scene.world_render_origin

        pygame.draw.rect(self.game_object.scene.app.window, (255, 0, 0), 
                         (self.game_object.position.x + wro.x, 
                          self.game_object.position.y + wro.y, 8, 8))
        
class DrawDummy(Component):
    def __init__(self, parent_game_object) -> None:
        super().__init__("DrawDummy", parent_game_object)
        
    def draw(self):
        wro = self.game_object.scene.world_render_origin
        print("Im rendering it")

        pygame.draw.rect(self.game_object.scene.app.window, (0, 255, 0), 
                         (self.game_object.position.x + wro.x, 
                          self.game_object.position.y + wro.y, 8, 8))