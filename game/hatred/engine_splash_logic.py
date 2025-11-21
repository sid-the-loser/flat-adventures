import pygame

from hatred.component import Component
from hatred.game_details import ENGINE_SPLASH_TIME, WINDOW_SIZE

font = pygame.font.SysFont(None, 72)

class SplashImage(Component):
    def __init__(self, parent_game_object, active: bool = True) -> None:
        super().__init__("SplashImage", parent_game_object, active)
        self.timer = 0
        self.logo_color = (255, 0, 0)
        self.current_color = (0, 0, 0)
        self.color_scale = 0
        
        self.splash_img = font.render("HATRED", False, self.current_color)
        self.splash_rect = self.splash_img.get_rect(center=(WINDOW_SIZE[0]/2,
                                                            WINDOW_SIZE[1]/2))

    def init(self):
        self.logo_color = (255, 0, 0)
        self.current_color = (0, 0, 0)
        self.splash_img = font.render("HATRED", False, self.current_color)

    def update(self):
        events = self.game_object.scene.app.events
        delta = self.game_object.scene.app.delta_time

        self.timer += delta

        self.color_scale = (self.timer*2) / ENGINE_SPLASH_TIME
        if self.color_scale > 1:
            self.color_scale = 1

        if self.color_scale < 0:
            print("less!", self.color_scale)
        elif self.color_scale > 255:
            print("more", self.color_scale)
        else:
            print("just right")

        self.current_color = (round(self.logo_color[0] * self.color_scale),
                              round(self.logo_color[1] * self.color_scale),
                              round(self.logo_color[2] * self.color_scale))
        
        print(self.current_color)
        
        if self.timer > ENGINE_SPLASH_TIME:
            self.switch_to_next()
        else:
            self.splash_img = font.render("HATRED", False, self.current_color)

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.switch_to_next()

    def draw(self):
        self.game_object.scene.app.window.blit(self.splash_img, self.splash_rect)
        
    def switch_to_next(self):
        self.game_object.scene.app.switch_to_scene_index(1)