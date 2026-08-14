from ...Kernel.Components.Graphical import Color4
from ...Kernel.Kernel import paths, ClassWrapper
from ..Camera.Camera2D import Camera2D
from ..Shaders.ShaderReader import ShaderReader
from ..Shaders.ShaderLoader import ShaderLoader
import os
import moderngl as mgl
import glm

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
        
        self.program["camera_matrix"].write(glm.mat4(1))
        if isinstance(self.window.camera, Camera2D):
            self.program["camera_matrix"].write(self.window.camera._camera_matrix(self.window))

        for render_item in self.window.to_render:
            if render_item.texture:
                render_item.texture.use(0)
                self.program["use_tex"].value = 1
            else:
                self.program["use_tex"].value = 0

            render_item.vao.render(mgl.TRIANGLE_FAN)

        self.window.to_render.clear()
