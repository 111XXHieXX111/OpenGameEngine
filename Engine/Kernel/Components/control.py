from ..modules import glfw, Enum

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

class kEvent(Enum):
    justP = "JustPressed"
    Pres = "Pressed"

class mEvent(Enum):
    Pres = "Pressed"
    Rel = "Released"

class Keys:
    W = Key("w")
    S = Key("s")
    A = Key("a")
    D = Key("d")

    UP = Key("up")
    DOWN = Key("down")
    LEFT = Key("left")
    RIGHT = Key("right")

    SPACE = Key("space")
    ESC = Key("escape")
    TAB = Key("tab")

    SHIFT = Key("shift")
    CONTROL = Key("control")
    ALT = Key("alt")

    K1 = Key("1")
    K2 = Key("2")
    K3 = Key("3")
    K4 = Key("4")
    K5 = Key("5")
    K6 = Key("6")
    K7 = Key("7")
    K8 = Key("8")
    K9 = Key("9")
    K0 = Key("0")
    