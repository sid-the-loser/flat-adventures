# This file will only be containing the interface code that the server owner
# be interacting with.

import threading

# I split the code into multiple different files, so theres a chance you might
# find some random modules with no extra functionality lying around. They're all
# blocks of code. They serve no function but to run and die.

import config_loader # loads the server configuration and can be used later to
                     # get configuration information.