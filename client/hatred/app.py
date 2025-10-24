import pygame
import game_details

class App:
    def __init__(self) -> None:
        """
        DO NOT OVERRIDE!
        """

        self.window = pygame.display.set_mode(game_details.WINDOW_SIZE)
        
        pygame.display.set_caption(f"{game_details.GAME_NAME} - {game_details.GAME_VERSION}")

        self.game_running = True

        self.init()
        self._loop()

    def _loop(self) -> None:
        """
        DO NOT OVERRIDE!
        """
        while self.game_running:
            pass

    def init(self) -> None:
        """
        This is an overridable function that runs when the game 
        initialises.
        """
        pass

    def update(self) -> None:
        """
        This is an overridable function that runs when the game updates every 
        tick.
        """