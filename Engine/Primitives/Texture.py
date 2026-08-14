from ..Kernel.Kernel import ClassWrapper

@ClassWrapper
class Texture:
    @staticmethod
    def Set(Object, Texture):
        Object.texture = Texture
    
    @staticmethod
    def Remove(Object):
        Object.texture = None
