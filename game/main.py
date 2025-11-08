import os
import pygame

import hatred
import hatred.app
import hatred.scene
import hatred.game_object
import hatred.component

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

myApp = hatred.app.App()

s_test = hatred.scene.Scene("test", myApp)

go_player = hatred.game_object.GameObject("player", s_test)

myApp.switch_to_scene("test")

myApp.run()