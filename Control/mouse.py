from ..Core.modules import glfw
from ..Core.base import Vec2, MouseButton

class Mouse:
    @staticmethod
    def getPosition(window):
        x, y = glfw.get_cursor_pos(window)
        return Vec2(x, y)
    
    @staticmethod
    def MouseKeyPressed(window, button:MouseButton):
        return glfw.get_mouse_button(window, button) == glfw.PRESS

    @staticmethod
    def MouseKeyReleased(window, button:MouseButton):
        return glfw.get_mouse_button(window, button) == glfw.RELEASE
    
    @staticmethod
    def setVisibility(window, visible:bool):
        glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_NORMAL if visible else glfw.CURSOR_HIDDEN)