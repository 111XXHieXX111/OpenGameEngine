from ...Kernel.Components.Graphical import Vertex, Color4
from ...Kernel.Components.Vectors import Vec2, Vec3
from ...Kernel.Kernel import ClassWrapper
from ..Base import Base, Base3D

@ClassWrapper
class Quad(Base, Base3D):
    def __init__(self):
        super().__init__()
        self.vertices_config = (
            (0.0, 0.0, 0.0),
            (1.0, 0.0, 0.0),
            (0.0, 1.0, 0.0),
            (1.0, 0.0, 0.0),
            (1.0, 1.0, 0.0),
            (0.0, 1.0, 0.0)
        )

        self.uv = [ 
            Vec2(0.0, 0.0),
            Vec2(1.0, 0.0),
            Vec2(1.0, 1.0),
            Vec2(1.0, 0.0),
            Vec2(1.0, 1.0),
            Vec2(0.0, 1.0)
        ]

        self._build_vao()
        self._build_model()
