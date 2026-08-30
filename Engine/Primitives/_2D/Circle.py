from ...Kernel.Components.Graphical import Vertex, Color4
from ...Kernel.Components.Vectors import Vec2, Vec3
from ...Kernel.Kernel import ClassWrapper
from ..Base import Base, Base2D
import math

@ClassWrapper
class Circle(Base, Base2D):
    def __init__(self, s:int=32):
        super().__init__()
        self.vertices_config = self._gen_circle_config(s)

        self.uv = self._gen_uv(s)

        self._build_vao()

    def _gen_circle_config(self, segments):
        points = []
        for i in range(segments):
            t = 2 * math.pi * i / segments
            x = (math.cos(t) + 1) / 2
            y = (math.sin(t) + 1) / 2
            points.append((x, y, 0.0))
        return tuple(points)

    def _gen_uv(self, segments:int):
        uv = []
        for i in range(segments):
            t = 2 * math.pi * i / segments
            u = (math.cos(t) + 1) / 2
            v = (math.sin(t) + 1) / 2
            uv.append(Vec2(u, v))
        return uv
