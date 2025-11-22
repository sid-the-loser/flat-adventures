import os

import hatred
import hatred.app
import hatred.scene
import hatred.game_object

import global_components
import main_menu_components

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

ASSETS_PATH = os.path.join(BASE_PATH, "assets/")

if os.path.exists(ASSETS_PATH):
    pass

myApp = hatred.app.App()

global_components.DebugKeyLogic(myApp)
c_config = global_components.ConfigForP2P(myApp, os.path.join(ASSETS_PATH, "config.yaml")) # TODO: work on multiplayer

# Scene : Main Menu

s_main_menu = hatred.scene.Scene("MainMenu", myApp)

go_title_label = hatred.game_object.GameObject("TitleLabel", s_main_menu)
main_menu_components.TitleLabel(go_title_label)

# Scene : Singleplayer Menu

s_singleplayer = hatred.scene.Scene("SingleplayerMenu", myApp)

# Scene : Multiplayer Menu

s_multiplayer = hatred.scene.Scene("MultiplayerMenu", myApp)

# App loop

myApp.run()