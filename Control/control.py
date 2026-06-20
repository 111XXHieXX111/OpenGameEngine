from ..Core.modules import keyboard
from ..Core.base import Key

_pressed = {}

def KeyPressed(key:Key):
    
    # CHECK TYPE
    
    if not isinstance(key, Key):
        return False
    
    # RETURN STATE
    
    if key:
        return keyboard.is_pressed(key.key)

def KeyJustPressed(key: Key):
    
    # CHECK TYPE
    
    if not isinstance(key, Key):
        return False
    
    current = keyboard.is_pressed(key.key)
    
    if current and not _pressed.get(key.key, False):
        _pressed[key.key] = True
        return True
    
    if not current:
        _pressed[key.key] = False
    
    return False