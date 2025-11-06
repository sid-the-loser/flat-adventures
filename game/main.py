import os

import hatred
import hatred.app
import hatred.scene

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

myApp = hatred.app.App()

test_scene = hatred.scene.Scene("gay ass", myApp)

myApp.switch_to_scene("gay ass")

myApp.run()