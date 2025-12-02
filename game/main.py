from random import randint
from _thread import start_new_thread

from hatred.app import App
from hatred.scene import Scene
from hatred.game_object import GameObject

from scripts.global_components import GlobalKeys
from scripts.main_menu_components import Title, Background, SubTitle
from scripts.gameplay_componenets import PlayerMovement, RenderPawn, BackgroundColor, DummyMovement

myApp = App()

GlobalKeys(myApp)

s_main_menu = Scene("MainMenu", myApp)
go_main_menu_ui = GameObject("MainMenuUI", s_main_menu)
Background(go_main_menu_ui)
SubTitle(go_main_menu_ui)
Title(go_main_menu_ui)

s_gameplay = Scene("Gameplay", myApp)
go_misc_components = GameObject("MiscComponents", s_gameplay)
BackgroundColor(go_misc_components)

go_player = GameObject("Player", s_gameplay)
go_player.layer = 1
PlayerMovement(go_player)
RenderPawn(go_player, (0, 255, 0))

go_dummies: list[GameObject] = []

def create_dummies():
    global go_dummies
    gen = 100000
    spread = 10
    for i in range(gen):
        go_dummies.append(GameObject("Dummy", s_gameplay))
        go_dummies[-1].position.x = randint(-spread, spread)
        go_dummies[-1].position.y = randint(-spread, spread)
        RenderPawn(go_dummies[-1], (255, 0, 0))
        DummyMovement(go_dummies[-1])

    print(f"{gen}: done and closing!")

start_new_thread(create_dummies, tuple())

myApp.run()