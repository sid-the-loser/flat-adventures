import sys
import os

def get_base_path() -> str:
    """Get absolute path to resource, works for dev and PyInstaller."""
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        return sys._MEIPASS
    except AttributeError:
        return os.path.abspath(".")