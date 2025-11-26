import pygame
import os
import math

from hatred.component import Component
from hatred.math_plus import lerp

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

ASSETS_PATH = os.path.join(BASE_PATH, "assets/")

FONT_PATH = os.path.join(ASSETS_PATH, "fonts/Tiny5-Regular.ttf")

class TitleLabel(Component): # TODO: fix this! Not everything should be under the same umbrella
    def __init__(self, parent_game_object, active: bool = True) -> None:
        super().__init__("TitleLabel", parent_game_object, active)
        self.selected_button = 0

        self.title_font = pygame.font.Font(FONT_PATH, 72)
        self.subtitle_font = pygame.font.Font(FONT_PATH, 24)
        self.button_font = pygame.font.Font(FONT_PATH, 48)

        self.unselected_button_c = (200, 200, 200)
        self.selected_button_c = (255, 255, 0)

        self.title_img = self.title_font.render("Flat Adventures", False, 
                                                (255, 255, 255))
        self.subtitle_img = self.subtitle_font.render("Press any button to continue",
                                                      False, (255, 255, 0))
        self.singleplayer_button_img = self.button_font.render("Singleplayer", 
                                                               False, 
                                                                (200, 200, 200))
        self.multiplayer_button_img = self.button_font.render("Multiplayer", 
                                                              False, 
                                                              (200, 200, 200))
        self.quit_button_img = self.button_font.render("Quit", False, 
                                                       (200, 200, 200))
        
        self.title_rect = self.title_img.get_rect(center=(300, 300))
        self.subtitle_rect = self.subtitle_img.get_rect(center=(300, 400))
        self.singleplayer_button_rect = self.singleplayer_button_img.get_rect()
        self.multiplayer_button_rect = self.multiplayer_button_img.get_rect()
        self.quit_button_rect = self.quit_button_img.get_rect()

        self.animation_speed_x = self.title_rect.x / self.title_rect.y

        self.singleplayer_button_rect.y = 72
        self.multiplayer_button_rect.y = 72 + 48
        self.quit_button_rect.y = 72 + (48 * 2) # maybe use game object position ma guy

        self.title_triggered_flag = False
        self.render_buttons_flag = False

    def init(self):
        self.render_button_fonts()

    def update(self):
        global title_triggered_flag

        delta = self.game_object.scene.app.delta_time

        for event in self.game_object.scene.app.events:
            if event.type == pygame.KEYDOWN:
                if not self.title_triggered_flag:
                    self.title_triggered_flag = True

                else:
                    self.title_rect.x = 0
                    self.title_rect.y = 0

                if self.render_buttons_flag:
                    if event.key == pygame.K_RETURN:
                        self.okay_triggered()

                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.selected_button -= 1
                        self.blink_timer = 1
                        if self.selected_button < 0:
                            self.selected_button = 0
                        else:
                            self.render_button_fonts()

                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.selected_button += 1
                        self.blink_timer = 1
                        if self.selected_button > 2:
                            self.selected_button = 2
                        else:
                            self.render_button_fonts()
            
        if self.title_triggered_flag:
            if self.title_rect.x != 0 or self.title_rect.y != 0:
                self.title_rect.x = round(lerp(self.title_rect.x, 0, 
                                         delta * self.animation_speed_x), 3)
                self.title_rect.y = round(lerp(self.title_rect.y, 0, delta), 3)
            else:
                self.render_buttons_flag = True

    def draw(self):
        window = self.game_object.scene.app.window

        window.blit(self.title_img, self.title_rect)

        if not self.title_triggered_flag:
            window.blit(self.subtitle_img, self.subtitle_rect)

        if self.render_buttons_flag:
            window.blit(self.singleplayer_button_img, 
                        self.singleplayer_button_rect)
            window.blit(self.multiplayer_button_img, 
                        self.multiplayer_button_rect)
            window.blit(self.quit_button_img, 
                        self.quit_button_rect)

    def render_button_fonts(self):
        self.singleplayer_button_img = self.button_font.render("Singleplayer", 
                                                               False, 
                                                               self.unselected_button_c if self.selected_button != 0 else self.selected_button_c)
        self.multiplayer_button_img = self.button_font.render("Multiplayer", 
                                                              False, 
                                                              self.unselected_button_c if self.selected_button != 1 else self.selected_button_c)
        self.quit_button_img = self.button_font.render("Quit", False, 
                                                       self.unselected_button_c if self.selected_button != 2 else self.selected_button_c)
        
    def okay_triggered(self):
        if self.selected_button == 0:
            self.game_object.scene.app.switch_to_scene("Singleplayer")

        elif self.selected_button == 1:
            self.game_object.scene.app.switch_to_scene("Multiplayer")

        elif self.selected_button == 2:
            self.game_object.scene.app.quit_app()