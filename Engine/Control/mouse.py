from ..Kernel.modules import glfw
from ..Kernel.Components.vectors import Vec2
from ..Kernel.Components.control import MouseButton
from ..Kernel.kernel import classWrapper

@classWrapper
class Mouse:
    @staticmethod
    def getPosition(window):
        x, y = glfw.get_cursor_pos(window.window)
        return Vec2(x, y)
    
    @staticmethod
    def MouseKeyPressed(window, button:MouseButton):
        return glfw.get_mouse_button(window.window, button) == glfw.PRESS

    @staticmethod
    def MouseKeyReleased(window, button:MouseButton):
        return glfw.get_mouse_button(window.window, button) == glfw.RELEASE
    
    @staticmethod
    def setVisibility(window, visible:bool):
        glfw.set_input_mode(window.window, glfw.CURSOR, glfw.CURSOR_NORMAL if visible else glfw.CURSOR_HIDDEN)
