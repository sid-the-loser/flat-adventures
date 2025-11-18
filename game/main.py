import os

import hatred
import hatred.app
import hatred.scene
import hatred.game_object

import custom_components

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

ASSETS_PATH = os.path.join(BASE_PATH, "./assets/")

myApp = hatred.app.App()

s_splash_screen = hatred.scene.Scene("SplashScreen", myApp)

s_main_menu = hatred.scene.Scene("MainMenu", myApp)

myApp.switch_to_scene("SplashScreen")
myApp.run()