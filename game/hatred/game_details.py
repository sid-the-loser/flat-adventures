import pygame

GAME_NAME: str = "flat adventures"
GAME_VERSION: str = "ea0.0.1"

WINDOW_SIZE: tuple = (600, 600)
WINDOW_FLAGS: int = pygame.RESIZABLE | pygame.SCALED
WINDOW_DEFAULT_DISPLAY: int = 0
WINDOW_VSYNC: int = 0
WINDOW_TITLE: str = f"{GAME_NAME} - {GAME_VERSION}"
WINDOW_ICON: str = "" # TODO: To be added later
WINDOW_FPS: int = 30 # limited to 30 to help with performance

# NOTE: Keep true when building the project
IS_BUILD: bool = False

ENGINE_SPLASH_TIME: float = 5