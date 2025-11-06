import os

import hatred
import hatred.app
import hatred.scene

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

myApp = hatred.app.App()

test_scene = hatred.scene.Scene("test", myApp)

myApp.switch_to_scene("test")

myApp.run()