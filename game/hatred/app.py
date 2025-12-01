import pygame

import hatred.scene
import hatred.game_details
import hatred.component
import hatred.engine_splash_logic
import hatred.game_object

# TODO: unified input event system!

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

        pygame.mouse.set_visible(False) # disables mouse visibility over window

        self.input_status: dict[int, dict[str, bool]] = {}

        tmp_input_map = hatred.game_details.INPUT_MAP

        for name in tmp_input_map:
            val = tmp_input_map[name]

            match val:
                case list():
                    for k in val:
                        if k not in self.input_status:
                            self.input_status[k] = {
                                "just_pressed": False,
                                "just_released": False,
                                "pressed" : False
                            }
                case int():
                    if val not in self.input_status:
                        self.input_status[val] = {
                            "just_pressed": False,
                            "just_released": False,
                            "pressed" : False
                        }

        self.global_components: list[hatred.component.GlobalComponent] = []

        self.scene_list: list[hatred.scene.Scene] = []

        self.clock = pygame.time.Clock()
        # this could lead to glitches, but this only persists the first frame of
        #  the app launching
        self.delta_time = 1

        self.events: list[pygame.Event] = pygame.event.get()

        self.app_running: bool = True

        # NOTE: splash screen logic at the end works better and is safer

        s_engine_splash = hatred.scene.Scene("EngineSplash", self)
        go_splash_text = hatred.game_object.GameObject("SplashText", s_engine_splash)
        hatred.engine_splash_logic.SplashImage(go_splash_text)

        self.current_scene: hatred.scene.Scene

        self.switch_to_scene("EngineSplash") # current scene gets updated here!

    def run(self):
        for g_comp in self.global_components:
            g_comp.init()

        while self.app_running:
            self.delta_time: float = self.clock.tick(
                hatred.game_details.WINDOW_FPS) / 1000

            for k in self.input_status:
                self.input_status[k]["just_pressed"] = False
                self.input_status[k]["just_released"] = False

            self.events: list[pygame.Event] = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    self.quit_app()

                elif event.type == pygame.KEYDOWN:
                    for k in self.input_status:
                        if event.key == k:
                            self.input_status[k]["just_pressed"] = True
                            self.input_status[k]["pressed"] = True

                elif event.type == pygame.KEYUP:
                    for k in self.input_status:
                        if event.key == k:
                            self.input_status[k]["just_released"] = True
                            self.input_status[k]["pressed"] = False
                            

            for g_comp in self.global_components:
                g_comp.early_update()

            self.current_scene.update()

            for g_comp in self.global_components:
                g_comp.late_update()

            self.window.fill((255, 0, 255))
            pygame.draw.rect(self.window, (0, 0, 0), (0, 0, 300, 300))
            pygame.draw.rect(self.window, (0, 0, 0), (300, 300, 300, 300))

            for g_comp in self.global_components:
                g_comp.early_draw()

            self.current_scene.draw()

            for g_comp in self.global_components:
                g_comp.late_draw()

            pygame.display.flip()

        pygame.quit()

    def quit_app(self):
        self.app_running = False

    def add_scene(self, scene: hatred.scene.Scene) -> None:
        potential_index: int = self.find_scene_index_by_name(scene.name)
        if potential_index >= 0:
            raise SceneNameAlreadyInUseError(
                f"\"{scene.name}\" is already in use by another scene at scene_list[{potential_index}]")

        self.scene_list.append(scene)

    def remove_scene(self, scene_name: str) -> None:
        for i in range(len(self.scene_list)):
            if self.scene_list[i].name == scene_name:
                self.scene_list.pop(i)
                break
        else:
            raise SceneNameError(f"\"{scene_name}\" could not be found!")
        
    def find_scene_index_by_name(self, scene_name: str) -> int:
        for i in range(len(self.scene_list)):
            if self.scene_list[i].name == scene_name:
                return i
        else:
            return -1
        
    def switch_to_scene_index(self, index: int) -> None:
        length = len(self.scene_list)

        if length < index+1:
            raise SceneIndexOutOfRangeError(
                f"Index ({index}) is out of range since scene_list\'s length is: {length}"
                )
        
        for i in range(length):
            if i != index:
                self.scene_list[i].active = False
            else:
                self.current_scene = self.scene_list[i]
                self.scene_list[i].active = True
                self.scene_list[i].init()

    def switch_to_scene(self, scene_name: str) -> None:
        if self.find_scene_index_by_name(scene_name) < 0:
            raise SceneNameError(f"\"{scene_name}\" could not be found!")

        for _s in self.scene_list:
            if _s.name != scene_name:
                _s.active = False
            else:
                self.current_scene = _s
                _s.active = True
                _s.init()

    def add_global_component(self, 
                             global_component: hatred.component.GlobalComponent):
        potential_index = self.find_global_component_index(
            global_component.name)
        if potential_index > -1:
            raise GlobalComponentAlreadyExistsError(
                f"{global_component.name} already exists in app at index: {potential_index}")
        
        self.global_components.append(global_component)

    def find_global_component_index(self, name: str) -> int:
        for i in range(len(self.global_components)):
            if name == self.global_components[i].name:
                return i
            
        return -1
    
    def input_is_pressed(self, event_name: str) -> bool:
        input_map = hatred.game_details.INPUT_MAP

        if event_name in input_map:
            pressed_flag = False

            value = input_map[event_name]

            match value:
                case list():
                    value = list(value)

                case int():
                    value = [value, ]

            for v in value:
                if not self.input_status[v]["pressed"]:
                    break
            else:
                pressed_flag = True

            return pressed_flag

        else:
            raise InputIDNotInInputMapError(f"{event_name} not found in INPUT_MAP")
        
    def input_is_just_pressed(self, event_name: str) -> bool:
        input_map = hatred.game_details.INPUT_MAP

        if event_name in input_map:
            pressed_flag = False

            value = input_map[event_name]

            match value:
                case list():
                    value = list(value)

                case int():
                    value = [value, ]

            for v in value:
                if not self.input_status[v]["just_pressed"]:
                    break
            else:
                pressed_flag = True

            return pressed_flag

        else:
            raise InputIDNotInInputMapError(f"{event_name} not found in INPUT_MAP")
        
    def input_is_just_released(self, event_name: str) -> bool:
        input_map = hatred.game_details.INPUT_MAP

        if event_name in input_map:
            pressed_flag = False

            value = input_map[event_name]

            match value:
                case list():
                    value = list(value)

                case int():
                    value = [value, ]

            for v in value:
                if not self.input_status[v]["just_released"]:
                    break
            else:
                pressed_flag = True

            return pressed_flag

        else:
            raise InputIDNotInInputMapError(f"{event_name} not found in INPUT_MAP")

# Errors

class SceneNameError(Exception):
    pass

class SceneIndexOutOfRangeError(Exception):
    pass

class SceneNameAlreadyInUseError(Exception):
    pass

class GlobalComponentAlreadyExistsError(Exception):
    pass

class NoSceneAfterSplashScreenError(Exception): # TODO: seems neesh, not used rn, might remove later
    pass

class InputIDNotInInputMapError(Exception):
    pass