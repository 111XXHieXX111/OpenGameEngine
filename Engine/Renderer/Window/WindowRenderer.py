from ...Kernel.Components.Graphical import Color4
from ...Kernel.Kernel import paths, ClassWrapper
from ...Primitives.Base import DType
from ..Camera.Camera2D import Camera2D
from ..Camera.Camera3D import Camera3D
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
        self.mat4x4_1 = glm.mat4(1)

    def LoadBaseShader(self):
        vertex_shader, fragment_shader = ShaderReader(os.path.join(paths["Shaders"], "BaseColor.vert"), os.path.join(paths["Shaders"], "BaseColor.frag"))
        self.program = ShaderLoader(vertex_shader, fragment_shader)

    def Renderer(self):
        self.context.clear(self.fillcolor.r, self.fillcolor.g, self.fillcolor.b, self.fillcolor.a, 1.0)

        self.context.enable(mgl.BLEND)

        winsize = self.window.current_window_sizes
        
        self.context.viewport = (0, 0, winsize.x, winsize.y)
        
        notexture_enabled = self.window.infomonitor.notexture_enabled
        
        if isinstance(self.window.camera, Camera2D):
            self.program["camera"].value = 1
            self.program["camera_matrix"].write(self.window.camera._camera_matrix(self.window))
        elif isinstance(self.window.camera, Camera3D):
            view, proj = self.window.camera._get(self.window)
            self.program["camera"].value = 2
            self.program["view"].write(view)
            self.program["proj"].write(proj)
        else:
            self.program["camera"].value = 0
        
        self.window.to_render.sort(key=lambda item: item.layer)
        
        for render_item in self.window.to_render:
            if render_item.texture and not notexture_enabled:
                render_item.texture.use(0)
                self.program["use_tex"].value = 1
            else:
                self.program["use_tex"].value = 0
            
            self.program["model"].write(render_item.model)
            self.program["vertex_color"].value = (render_item.color.r, render_item.color.g, render_item.color.b, render_item.color.a)
            
            if render_item.dtype == DType._3D:
                self.context.enable(mgl.DEPTH_TEST)
                render_item.vao.render(mgl.TRIANGLES)
            elif render_item.dtype == DType._2D:
                self.context.disable(mgl.DEPTH_TEST)
                render_item.vao.render(mgl.TRIANGLE_FAN)

        self.window.to_render.clear()
