from ...Kernel.Components.Graphical import Color4
from ...Kernel.Kernel import paths, ClassWrapper
from ...Primitives.Base import DType
from ..Camera.Camera2D import Camera2D
from ..Camera.Camera3D import Camera3D
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
        self.material = None
    
    def LoadBaseShader(self):
        vertex_shader, fragment_shader = ShaderReader(os.path.join(paths["Shaders"], "BaseColor.vert"), os.path.join(paths["Shaders"], "BaseColor.frag"))
        self.program = ShaderLoader(vertex_shader, fragment_shader)

    def LoadMaterial3DShader(self):
        vertex_shader, fragment_shader = ShaderReader(os.path.join(paths["Shaders"], "3DMaterial.vert"), os.path.join(paths["Shaders"], "3DMaterial.frag"))
        self.material = ShaderLoader(vertex_shader, fragment_shader)

    def Renderer(self):
        self.context.clear(self.fillcolor.r, self.fillcolor.g, self.fillcolor.b, self.fillcolor.a, 1.0)

        self.context.enable(mgl.BLEND)

        winsize = self.window.current_window_sizes
        
        self.context.viewport = (0, 0, winsize.x, winsize.y)
        
        notexture_enabled = self.window.infomonitor.notexture_enabled
        
        _set_camera_for_shader(self, self.material)
        _set_camera_for_shader(self, self.program)
        
        self.window.to_render.sort(key=lambda item: item.layer)
        
        for render_item in self.window.to_render:
            if render_item.material and self.material:
                shader = self.material
            else:
                shader = self.program

            if render_item.texture and not notexture_enabled:
                render_item.texture.use(0)
                shader["use_tex"].value = 1
            else:
                shader["use_tex"].value = 0
            
            shader["model"].write(render_item.model)

            if render_item.material:
                shader["vertex_color"].value = (render_item.material.color.r, render_item.material.color.g, render_item.material.color.b, render_item.material.color.a)
            else:
                shader["vertex_color"].value = (render_item.color.r, render_item.color.g, render_item.color.b, render_item.color.a)

            if render_item.material and self.material:
                ambient_color = render_item.material.ambient_color
                light_pos = render_item.material.light_pos
                light_color = render_item.material.light_color

                shader["ambient_light"].value = (ambient_color.r, ambient_color.g, ambient_color.b)
                shader["light_position"].value = (light_pos.x, light_pos.y, light_pos.z)
                shader["light_color"].value = (light_color.r, light_color.g, light_color.b)

            if render_item.dtype == DType._3D:
                self.context.enable(mgl.DEPTH_TEST)
                render_item.vao.render(mgl.TRIANGLES)
            elif render_item.dtype == DType._2D:
                self.context.disable(mgl.DEPTH_TEST)
                render_item.vao.render(mgl.TRIANGLE_FAN)

        self.window.to_render.clear()

def _set_camera_for_shader(self:WindowRenderer, shader):
    if isinstance(self.window.camera, Camera2D):
        shader["camera"].value = 1
        shader["camera_matrix"].write(self.window.camera._camera_matrix(self.window))
    elif isinstance(self.window.camera, Camera3D):
        view, proj = self.window.camera._get(self.window)
        shader["camera"].value = 2
        shader["view"].write(view)
        shader["proj"].write(proj)
    else:
        shader["camera"].value = 0
