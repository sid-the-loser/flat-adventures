import os
import pygame
import yaml

from hatred.component import Component, GlobalComponent
from global_components import ServerModel

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

ASSETS_PATH = os.path.join(BASE_PATH, "assets/")

FONT_PATH = os.path.join(ASSETS_PATH, "fonts/Tiny5-Regular.ttf")

menu_open = True

class TextLabel(Component):
    def __init__(self, parent_game_object, active: bool = True) -> None:
        super().__init__("TextLabel", parent_game_object, active)
        self.label_font = pygame.font.Font(FONT_PATH, 72)
        self.label_img = self.label_font.render("Multiplayer", False, 
                                                (255, 255, 255))
        self.label_rect = self.label_img.get_rect()

    def init(self):
        global menu_open

        menu_open = True

    def update(self):
        if menu_open:
            self.label_rect.x = self.game_object.position.x
            self.label_rect.y = self.game_object.position.y

    def draw(self):
        if menu_open:
            window = self.game_object.scene.app.window
            window.blit(self.label_img, self.label_rect)

class Entry(Component):
    def __init__(self, parent_game_object, active: bool = True) -> None:
        super().__init__("Entry", parent_game_object, active)

        self.label_font = pygame.font.Font(FONT_PATH, 8)
        self.label_img = self.label_font.render("Enter text here", False, 
                                                (255, 255, 255))
        self.label_rect = self.label_img.get_rect()

        self.text = ""

        self.game_object.position.y = 100

        self.global_server: GlobalComponent | ServerModel | None = None

    def init(self):
        self.label_img = self.label_font.render("Enter text here", False, 
                                                (255, 255, 255))
        self.label_rect = self.label_img.get_rect()
        self.text = ""

        self.global_server = \
            self.game_object.scene.app.global_components[self.game_object.scene.app.find_global_component_index("ServerModel")]

    def update_text(self):
        self.label_img = self.label_font.render(self.text, False, 
                                                (255, 255, 255))
        self.label_rect = self.label_img.get_rect()

    def update(self):
        global menu_open
        if menu_open:
            self.label_rect.x = self.game_object.position.x
            self.label_rect.y = self.game_object.position.y

            events = self.game_object.scene.app.events

            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # TODO: make shit connect
                        menu_open = False
                    else:
                        text: str = event.unicode
                        if text.isalpha():
                            self.text += text
                            self.update_text()
    
    def draw(self):
        if menu_open:
            window = self.game_object.scene.app.window
            window.blit(self.label_img, self.label_rect)

class DrawDummy(Component):
    def __init__(self, parent_game_object) -> None:
        super().__init__("DrawDummy", parent_game_object)
        self.name = ""

        self.label_font = pygame.font.Font(FONT_PATH, 72)

        self.name_img = self.label_font.render(self.name, False, 
                                                (255, 255, 255))
        
        self.name_rect = self.name_img.get_rect()

    def update_name(self, name: str):
        self.name = name
        self.name_img = self.label_font.render(self.name, False, 
                                                (255, 255, 255))
        
        self.name_rect = self.name_img.get_rect()

    def update(self):
        self.name_rect.x = self.game_object.position.x
        self.name_rect.y = self.game_object.position.y
        
    def draw(self) -> None:
        wro = self.game_object.scene.world_render_origin
        window = self.game_object.scene.app.window

        pygame.draw.rect(window, (0, 255, 0), 
                         (self.game_object.position.x + wro.x, 
                          self.game_object.position.y + wro.y, 8, 8))