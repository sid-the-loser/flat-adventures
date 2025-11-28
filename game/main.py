from hatred.app import App
from hatred.scene import Scene

from scripts.global_components import GlobalKeys

myApp = App()

GlobalKeys(myApp)

s_main_menu = Scene("MainMenu", myApp)

myApp.run()