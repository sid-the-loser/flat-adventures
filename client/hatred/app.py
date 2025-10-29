# External dependencies
import pygame
import sys
import scene

# In-codebase dependencies
import game_details

class App:
    def __init__(self) -> None:
        self.window: pygame.Surface = pygame.display.set_mode(
            size=game_details.WINDOW_SIZE, 
            flags=game_details.WINDOW_FLAGS,
            display=game_details.WINDOW_DEFAULT_DISPLAY,
            vsync=game_details.WINDOW_VSYNC
            )
        pygame.display.set_caption(game_details.GAME_VERSION)

        # TODO: Value not populated in game_details
        # window_icon_surface = pygame.image.load(game_details.WINDOW_ICON)
        # pygame.display.set_icon(window_icon_surface)

        self.scene_list: list[scene.Scene] = []
        self.current_scene: scene.Scene | None = None

        self.app_running = True

    def quit_app(self):
        pass

    def add_scene(self, scene_name: str) -> None:
        potential_index: int = self.find_scene_by_name(scene_name)
        if potential_index >= 0:
            raise SceneNameAlreadyInUse(
                f"\"{scene_name}\" is already in use by another scene at scene_list[{potential_index}]")

        self.scene_list.append(scene.Scene(scene_name))

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

# Signals



# Errors

class SceneNameError(Exception):
    pass

class SceneNameAlreadyInUse(Exception):
    pass