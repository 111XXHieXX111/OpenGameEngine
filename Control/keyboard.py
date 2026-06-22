from ..Core.modules import keyboard
from ..Core.base import Key

_pressed = {}

class Keyboard:
    @staticmethod
    def KeyPressed(key:Key, window=None):
        
        # CHECK ICONIFY
        
        if window:
            if window.iconified:
                if window.iconifiedwork:
                    return
        
        # CHECK TYPE
        
        if not isinstance(key, Key):
            return False
        
        # RETURN STATE
        
        if key:
            return keyboard.is_pressed(key.key)

    @staticmethod
    def KeyJustPressed(key:Key, window=None):
        
        # CHECK ICONIFY
        
        if window:
            if window.iconified:
                if window.iconifiedwork:
                    return
        
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