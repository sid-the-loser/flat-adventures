import pygame
import sys

import hatred.scene
import hatred.game_details

class App:
    def __init__(self) -> None:
        self.window: pygame.Surface = pygame.display.set_mode(
            size=hatred.game_details.WINDOW_SIZE, 
            flags=hatred.game_details.WINDOW_FLAGS,
            display=hatred.game_details.WINDOW_DEFAULT_DISPLAY,
            vsync=hatred.game_details.WINDOW_VSYNC
            )
        pygame.display.set_caption(hatred.game_details.WINDOW_TITLE)

        # TODO: Value not populated in hatred.game_details
        # window_icon_surface = pygame.image.load(hatred.game_details.WINDOW_ICON)
        # pygame.display.set_icon(window_icon_surface)

        self.scene_list: list[hatred.scene.Scene] = [
            hatred.scene.Scene("blank", self)
        ]
        self.current_scene: hatred.scene.Scene = self.scene_list[0]

        self.clock = pygame.time.Clock()
        # this could lead to glitches, but this only persists the first frame of
        #  the app launching
        self.delta_time = 1

        self.events: list[pygame.Event] = pygame.event.get()

        self.FILL_COLOR: tuple = (0, 0, 0)

        self.app_running: bool = True

    def run(self):
        while self.app_running:
            self.delta_time: float = self.clock.tick(
                hatred.game_details.WINDOW_FPS) / 1000

            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.quit_app()

            self.current_scene.update()

            self.window.fill(self.FILL_COLOR)

            self.current_scene.draw()

            pygame.display.flip()

        pygame.quit()

    def quit_app(self):
        self.app_running = False

    def add_scene(self, scene_name: str) -> None:
        potential_index: int = self.find_scene_by_name(scene_name)
        if potential_index >= 0:
            raise SceneNameAlreadyInUse(
                f"\"{scene_name}\" is already in use by another scene at scene_list[{potential_index}]")

        self.scene_list.append(hatred.scene.Scene(scene_name, self))

    def remove_scene(self, scene_name: str) -> None:
        for i in range(len(self.scene_list)):
            if self.scene_list[i].name == scene_name:
                self.scene_list.pop(i)
                break
        else:
            raise SceneNameError(f"\"{scene_name}\" could not be found!")
        
    def find_scene_by_name(self, scene_name: str) -> int:
        for i in range(len(self.scene_list)):
            if self.scene_list[i].name == scene_name:
                return i
        else:
            return -1

    def switch_to_scene(self, scene_name: str) -> None:
        if self.find_scene_by_name(scene_name) < 0:
            raise SceneNameError(f"\"{scene_name}\" could not be found!")

        for _s in self.scene_list:
            if _s.name != scene_name:
                _s.active = False
            else:
                _s.active = True
                self.current_scene = _s

# Errors

class SceneNameError(Exception):
    pass

class SceneNameAlreadyInUse(Exception):
    pass