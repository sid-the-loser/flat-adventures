import os

import hatred
import hatred.app

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

myApp = hatred.app.App()

myApp.remove_scene("blank")

print("Done")

myApp.run()