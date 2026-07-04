from ..modules import glfw

class Key:
    __slots__ = ("key")
    
    def __init__(self, key:str):
        self.key = key
    
    def getKey(self):
        return self.key

class MouseButton:
    LEFT = glfw.MOUSE_BUTTON_LEFT
    RIGHT = glfw.MOUSE_BUTTON_RIGHT
    MIDDLE = glfw.MOUSE_BUTTON_MIDDLE
    BUTTON_4 = glfw.MOUSE_BUTTON_4
    BUTTON_5 = glfw.MOUSE_BUTTON_5
    BUTTON_6 = glfw.MOUSE_BUTTON_6
    BUTTON_7 = glfw.MOUSE_BUTTON_7
    BUTTON_8 = glfw.MOUSE_BUTTON_8