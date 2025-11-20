import pygame

from hatred.component import GlobalComponent

class FunctionKeyLogic(GlobalComponent):
    def __init__(self, parent_app) -> None:
        super().__init__("DebugEvents", parent_app)
        self.show_debug_overlay = False

    def early_update(self) -> None:
        events = self.app.events

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F2:
                    pass # TODO: screenshot functionality

                if event.key == pygame.K_F3:
                    self.show_debug_overlay = not self.show_debug_overlay

                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()
                    # NOTE: This function works really badly with some display drivers is you are using pygame 1
