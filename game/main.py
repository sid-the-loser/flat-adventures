import os

import hatred
import hatred.app
import hatred.scene
import hatred.game_object
import hatred.component

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

myApp = hatred.app.App()

test_scene = hatred.scene.Scene("test", myApp)

player_object = hatred.game_object.GameObject("player", test_scene)

class WASDMovement(hatred.component.Component):
    pass

myApp.switch_to_scene("test")

myApp.run()