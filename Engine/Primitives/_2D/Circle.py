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

        self.vertices = self._gen_vertices(s)

        self._build_vao()

    def _gen_circle_config(self, segments):
        points = []
        for i in range(segments):
            t = 2 * math.pi * i / segments
            x = (math.cos(t) + 1) / 2
            y = (math.sin(t) + 1) / 2
            points.append((x, y))
        return tuple(points)
    
    def _gen_vertices(self, segments:int):
        vertices = []

        for _vertex_index in range(segments):
            idx = _vertex_index

            if idx == 0:
                idx = 1

            r = 1 / idx
            g = -(1 / idx) + 1
            b = abs(1 - 2 * idx / segments)

            vertex = Vertex(Vec3(0.0, 0.0, 0.0), Color4(r, g, b, 1.0), Vec2(0.0, 0.0))
            vertices.append(vertex)

        return vertices

    def _gen_uv(self, segments:int):
        uv = []
        for i in range(segments):
            t = 2 * math.pi * i / segments
            u = (math.cos(t) + 1) / 2
            v = (math.sin(t) + 1) / 2
            uv.append(Vec2(u, v))
        return uv
