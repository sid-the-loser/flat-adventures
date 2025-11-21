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

global_components.DebugKeyLogic(myApp)

s_main_menu = hatred.scene.Scene("MainMenu", myApp)

go_title_label = hatred.game_object.GameObject("TitleLabel", s_main_menu)
main_menu_components.TitleLabel(go_title_label)

s_single_player = hatred.scene.Scene("Singleplayer", myApp)

go_player = hatred.game_object.GameObject("Player", s_single_player)
player_components.PlayerControls(go_player)
player_components.DrawPlayer(go_player)
go_player.layer = 1
s_single_player.update_render_sort()

go_dummy = hatred.game_object.GameObject("Dummy", s_single_player)
player_components.DrawDummy(go_dummy)

myApp.run()