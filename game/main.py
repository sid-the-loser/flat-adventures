import os

import hatred
import hatred.app

BASE_PATH = os.path.abspath(__file__)

myApp = hatred.app.App()

# Evey logic in-between

myApp.run()