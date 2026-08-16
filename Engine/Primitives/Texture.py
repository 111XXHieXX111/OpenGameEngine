from ..Kernel.Components.Vectors import Vec2
from ..Kernel.Kernel import ClassWrapper

@ClassWrapper
class Texture:
    @staticmethod
    def Set(Object, Texture):
        Object.texture = Texture
    
    @staticmethod
    def Remove(Object):
        Object.texture = None

    @staticmethod
    def SetUV(Object, UV:list[Vec2, Vec2]):
        Object.uv = UV
        Object._build_vao()
