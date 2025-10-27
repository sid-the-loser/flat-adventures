import pygame
import sys

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

    def _stop_app(self):
        self.game_running = False

    def _force_stop_app(self, exit_code: sys._ExitCode):
        pygame.quit()
        sys.exit(exit_code)

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
        frame.
        """
        pass

    def tick_update(self) -> None:
        """
        This is an overridable function that runs when the game updates every 
        tick.
        """
        pass

    def render(self) -> None:
        """
        This is an overridable function that runs when the game updates every 
        frame.
        """
        pass

    def before_stop(self) -> None:
        """
        This is an overridable function that runs right before the game/app is about to
        close.
        """
        pass