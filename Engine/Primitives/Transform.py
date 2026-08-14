from ..Kernel.Components.Vectors import Vec2, Vec3
from ..Kernel.Kernel import ClassWrapper

@ClassWrapper
class Transform:
    @staticmethod
    def SetPosition(Object, Position:Vec2 | Vec3):
        if isinstance(Position, Vec2):
            Object.position = Position
        elif isinstance(Position, Vec3):
            pass

        Object._build_vao()

    @staticmethod
    def SetSize(Object, Size:Vec2 | Vec3):
        if isinstance(Size, Vec2):
            Object.size = Size
        elif isinstance(Size, Vec3):
            pass

        Object._build_vao()

    @staticmethod
    def Move(Object, Position:Vec2 | Vec3):
        if isinstance(Position, Vec2):
            Object.position += Position
        elif isinstance(Position, Vec3):
            pass

        Object._build_vao()

    @staticmethod
    def Scale(Object, Size:Vec2 | Vec3):
        if isinstance(Size, Vec2):
            Object.size *= Size
        elif isinstance(Size, Vec3):
            pass

        Object._build_vao()
