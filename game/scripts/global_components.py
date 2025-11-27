import pygame

from hatred.component import GlobalComponent

class GlobalKeys(GlobalComponent):
    def __init__(self, parent_app) -> None:
        super().__init__("GlobalKeys", parent_app)

    def early_update(self) -> None:
        pass