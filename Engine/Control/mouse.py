from ..Kernel.modules import glfw
from ..Kernel.Components.vectors import Vec2
from ..Kernel.Components.control import MouseButton
from ..Kernel.Components.graphics import stretchType
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
    
    @staticmethod
    def getMouseWorld(window):
        x, y = glfw.get_cursor_pos(window.window)
        win_w, win_h = window.current_window_sizes
        world_w = window.window_settings["width"]
        world_h = window.window_settings["height"]
        
        if window.window_settings["stretch"] == stretchType.KEEP_ASPECT:
            scale = min(win_w / world_w, win_h / world_h)
            offset_x = (win_w - (world_w * scale)) / 2
            offset_y = (win_h - (world_h * scale)) / 2
            return Vec2((x - offset_x) / scale,(y - offset_y) / scale)

        return Vec2(x * world_w / win_w,y * world_h / win_h)
