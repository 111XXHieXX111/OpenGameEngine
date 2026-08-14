from ..Renderer.Builder import Builder
from ..Renderer.Utils import pxtondc
from ..Kernel.Kernel import render_items, ClassWrapper, GetCurrentWindow
from ..Kernel.Components.Graphical import Vertex, Color4
from ..Kernel.Components.Vectors import Vec2, Vec3

@ClassWrapper
class Base:
    def __init__(self):
        super().__init__()
        self.window = GetCurrentWindow()
    
    def Draw(self):
        render_items.append(self)
        self.window.to_render.append(self)

@ClassWrapper
class Base2D:
    def __init__(self):
        self.vao = None
        self.vbo = None
        self.position = Vec2(0.0, 0.0)
        self.size = Vec2(0.0, 0.0)

    def _build_vao(self):
        if self.vao:
            self.vao.release()
        if self.vbo:
            self.vbo.release()

        ndc_vertices = []
        
        for index, vertex in enumerate(self.vertices_config):
            world_x = vertex[0] * self.size.x + self.position.x
            world_y = vertex[1] * self.size.y + self.position.y
            world_z = vertex[2] if len(vertex) > 2 else 0.0
            
            ndc_pos = pxtondc(Vec2(world_x, world_y), self.window)
            
            _vertex = Vertex(
                Vec3(ndc_pos.x, ndc_pos.y, world_z),
                Color4(
                    self.vertices[index].r,
                    self.vertices[index].g,
                    self.vertices[index].b,
                    self.vertices[index].a
                )
            )
            ndc_vertices.append(_vertex)

        self.vbo, self.vao = Builder(ndc_vertices)
