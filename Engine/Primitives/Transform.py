from ..Kernel.Components.Vectors import Vec1, Vec2, Vec3
from ..Kernel.Kernel import ClassWrapper

@ClassWrapper
class Transform:
    @staticmethod
    def SetPosition(Object, Position:Vec2 | Vec3):
        Object.position = Position
        Object._build_model()

    @staticmethod
    def SetSize(Object, Size:Vec2 | Vec3):
        Object.size = Size
        Object._build_model()

    @staticmethod
    def Move(Object, Position:Vec2 | Vec3):
        Object.position += Position
        Object._build_model()

    @staticmethod
    def Scale(Object, Size:Vec2 | Vec3):
        Object.size *= Size
        Object._build_model()

    @staticmethod
    def SetRotation(Object, Rotation:Vec1 | Vec3):
        Object.rotation = Rotation
        Object._build_model()

    @staticmethod
    def Rotate(Object, Rotation:Vec1 | Vec3):
        Object.rotation += Rotation
        Object._build_model()

    @staticmethod
    def GetPosition(Object):
        return Object.position

    @staticmethod
    def GetSize(Object):
        return Object.size
    