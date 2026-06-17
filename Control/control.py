from ..Core.modules import keyboard
from ..Core.base import Key

def KeyPressed(key:Key):
    if key:
        return keyboard.is_pressed(key.key)
