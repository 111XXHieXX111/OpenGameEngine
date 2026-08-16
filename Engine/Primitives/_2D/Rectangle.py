from ...Kernel.Components.Graphical import Vertex, Color4
from ...Kernel.Components.Vectors import Vec2, Vec3
from ...Kernel.Kernel import GetCurrentWindow, ClassWrapper
from ..Base import Base, Base2D

@ClassWrapper
class Rectangle(Base, Base2D):
    def __init__(self):
        super().__init__()
        self.vertices_config = (
            (0.0, 0.0, 0.0),
            (1.0, 0.0, 0.0),
            (1.0, 1.0, 0.0),
            (0.0, 1.0, 0.0)
        )
        
        self.uv = [ 
            Vec2(0.0, 0.0),
            Vec2(1.0, 0.0),
            Vec2(1.0, 1.0),
            Vec2(0.0, 1.0)
        ]

        self.vertices = [
            Vertex(Vec3(0.0, 0.0, 0.0), Color4(1.0, 0.0, 0.0, 1.0), Vec2(0.0, 0.0)),
            Vertex(Vec3(0.0, 0.0, 0.0), Color4(0.0, 1.0, 0.0, 1.0), Vec2(0.0, 0.0)),
            Vertex(Vec3(0.0, 0.0, 0.0), Color4(0.0, 0.0, 1.0, 1.0), Vec2(0.0, 0.0)),
            Vertex(Vec3(0.0, 0.0, 0.0), Color4(1.0, 0.0, 1.0, 1.0), Vec2(0.0, 0.0))
        ]

        self._build_vao()
