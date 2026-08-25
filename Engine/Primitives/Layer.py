from ..Kernel.Kernel import GetCurrentWindow, ClassWrapper

@ClassWrapper
class Layers:
    @staticmethod
    def Set(Object, Layer:int):
        Object.layer = Layer

    @staticmethod
    def Get(Object):
        return Object.layer
