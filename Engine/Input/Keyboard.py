from ..Kernel.Kernel import GetCurrentWindow, ClassWrapper
from ..Kernel.Components.Input import Keys
import glfw

_pressed = {}

@ClassWrapper
class _Keyboard:
    @staticmethod
    def KeyPressed(key:Keys):
        window = GetCurrentWindow()
        return bool(glfw.get_key(window.window, key))

    @staticmethod
    def KeyJustPressed(key:Keys):
        current = _Keyboard.KeyPressed(key)
        
        if current and not _pressed.get(key, False):
            _pressed[key] = True
            return True
        
        if not current:
            _pressed[key] = False
        
        return False

    @staticmethod
    def ConnectCallback(func, key:Keys):
        window = GetCurrentWindow()
        window.key_callbacks.append((key, func))
