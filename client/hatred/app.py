# External dependencies
import pygame
import sys

# In-codebase dependencies
import game_details

class App:
    def __init__(self):
        self.window: pygame.Surface = pygame.display.set_mode(
            size=game_details.WINDOW_SIZE, 
            flags=game_details.WINDOW_FLAGS,
            display=game_details.WINDOW_DEFAULT_DISPLAY,
            vsync=game_details.WINDOW_VSYNC
            )
        pygame.display.set_caption(game_details.GAME_VERSION)