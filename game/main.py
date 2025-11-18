import os

import hatred
import hatred.app
import hatred.scene
import hatred.game_object

import custom_components

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

myApp = hatred.app.App()

s_test = hatred.scene.Scene("test", myApp)

go_player = hatred.game_object.GameObject("player", s_test)
custom_components.DrawPlayer(go_player)
custom_components.PlayerControls(go_player)

dummy_player = hatred.game_object.GameObject("dummy", s_test)
custom_components.DrawDummy(dummy_player)

myApp.switch_to_scene("test")

myApp.run()