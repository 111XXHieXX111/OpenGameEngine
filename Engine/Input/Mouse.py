from ..Kernel.Components.Input import MouseButton
from ..Kernel.Components.Vectors import Vec2
from ..Kernel.Kernel import GetCurrentWindow, ClassWrapper
import glfw

@ClassWrapper
class _Mouse:
    @staticmethod
    def GetPosition():
        window = GetCurrentWindow()
        x, y = glfw.get_cursor_pos(window.window)
        return Vec2(x, y)
    
    @staticmethod
    def MouseKeyPressed(Button:MouseButton):
        window = GetCurrentWindow()
        return glfw.get_mouse_button(window.window, Button) == glfw.PRESS

    @staticmethod
    def MouseKeyReleased(Button:MouseButton):
        window = GetCurrentWindow()
        return glfw.get_mouse_button(window.window, Button) == glfw.RELEASE
