from ..Kernel import ClassWrapper
from ..Components.Vectors import Vec2, Vec3

@ClassWrapper
class Math:
    @staticmethod
    def Clamp(x:int|float, y:int|float, value:int|float):
        if value < x:
            return x
        elif value > y:
            return y
        return value

    @staticmethod
    def ClampVec2(x:int | float, y:int | float, vector:Vec2):
        x = Math.Clamp(x, y, vector.x)
        y = Math.Clamp(x, y, vector.y)
        return Vec2(x, y)
    
    @staticmethod
    def ClampVec3(x:int | float, y:int | float, vector:Vec3):
        x = Math.Clamp(x, y, vector.x)
        y = Math.Clamp(x, y, vector.y)
        z = Math.Clamp(x, y, vector.z)
        return Vec3(x, y, z)

    @staticmethod
    def GetDistanceVec2(x:Vec2, y:Vec2):
        dx = x.x - y.x
        dy = x.y - y.y
        return (dx*dx + dy*dy)**0.5

    @staticmethod
    def Lerp(a:str | float, b:str | float, t:int | float):
        return a + (b - a) * t
