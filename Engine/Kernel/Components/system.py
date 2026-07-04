from .graphics import Color3, Color4, c256
from .vectors import Vec2

class System:
    @staticmethod
    def check_empty(text:str):
        replaced_text = text.replace(' ', '')
        return replaced_text == ''

    @staticmethod
    def c3toc4(color:Color3 | Color4, a:float | c256 = 1.0):
        if isinstance(color, Color3):
            return Color4(color.r, color.g, color.b, a)
        elif isinstance(color, Color4):
            return Color4(color.r, color.g, color.b, color.a if a == 1.0 else a)
        else:
            log_system.addWarn("Use Color3|Color4")
            return Color4(0, 0, 0, 1)
    
    @staticmethod
    def slfm(x:int | float, y:int | float):
        return abs(x - y)

    @staticmethod
    def cltv2(l:list|tuple):
        if len(l) > 1:
            return Vec2(l[0], l[1])