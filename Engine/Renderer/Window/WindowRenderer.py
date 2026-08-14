from ...Kernel.Components.Graphical import Color4
from ...Kernel.Kernel import paths, ClassWrapper
from ..Shaders.ShaderReader import ShaderReader
from ..Shaders.ShaderLoader import ShaderLoader
import os
import moderngl as mgl

@ClassWrapper
class WindowRenderer():
    def __init__(self, window):
        self.context = mgl.create_context()
        self.fillcolor = Color4(0.1, 0.1, 0.1, 1.0)
        self.window = window
        self.program = None

    def LoadBaseShader(self):
        vertex_shader, fragment_shader = ShaderReader(os.path.join(paths["Shaders"], "BaseColor.vert"), os.path.join(paths["Shaders"], "BaseColor.frag"))
        self.program = ShaderLoader(vertex_shader, fragment_shader)

    def Renderer(self):
        self.context.clear(self.fillcolor.r, self.fillcolor.g, self.fillcolor.b, self.fillcolor.a)

        self.context.enable(mgl.BLEND)

        winsize = self.window.current_window_sizes
        
        self.context.viewport = (0, 0, winsize.x, winsize.y)

        for render_item in self.window.to_render:
            render_item.vao.render(mgl.TRIANGLE_FAN)

        self.window.to_render.clear()
