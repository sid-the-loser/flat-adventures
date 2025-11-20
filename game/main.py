import os

import hatred
import hatred.app
import hatred.scene
import hatred.game_object

import player_components
import global_components
import main_menu_components

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

ASSETS_PATH = os.path.join(BASE_PATH, "assets/")

myApp = hatred.app.App()

global_components.FunctionKeyLogic(myApp)

s_main_menu = hatred.scene.Scene("MainMenu", myApp)
go_title_label = hatred.game_object.GameObject("TitleLabel", s_main_menu)
main_menu_components.TitleLabel(go_title_label)

myApp.switch_to_scene("MainMenu")
myApp.run()