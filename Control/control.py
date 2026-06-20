from ..Core.modules import keyboard
from ..Core.base import Key
from ..Core.glob import log_system

def KeyPressed(key:Key):
    
    # CHECK TYPE
    
    if not isinstance(key, Key):
        return
    
    # RETURN STATE
    
    if key:
        return keyboard.is_pressed(key.key)
