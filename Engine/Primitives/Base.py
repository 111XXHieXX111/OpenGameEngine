from ..Renderer.Builder import Builder
from ..Kernel.Kernel import render_items, ClassWrapper, GetCurrentWindow, vaosvbos
from ..Kernel.Components.Vectors import Vec1, Vec2, Vec3
from ..Kernel.Components.Graphical import Color4
from .Misc.GFXObject import GFXObject
import glm

class DType:
    _3D = "3DDT"
    _2D = "2DDT"

@ClassWrapper
class Base(GFXObject):
    def __init__(self):
        super().__init__()
        self.InitObject()
        self.window = GetCurrentWindow()
        self.layer = 0
        self.model = glm.mat4(1)
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
        self.material = None
    
    def Draw(self):
        render_items.append(self)
        self.window.to_render.append(self)

    def _build_model(self):
        trans = glm.mat4(1.0)

        if isinstance(self.position, Vec3):
            trans = glm.translate(trans, glm.vec3(self.position.x, self.position.y, self.position.z))
        else:
            trans = glm.translate(trans, glm.vec3(self.position.x, self.position.y, 0.0))

        trans = glm.rotate(trans, glm.degrees(self.rotation.x), glm.vec3(1, 0, 0))
        if isinstance(self.rotation, Vec3):
            trans = glm.rotate(trans, glm.degrees(self.rotation.y), glm.vec3(0, 1, 0))
            trans = glm.rotate(trans, glm.degrees(self.rotation.z), glm.vec3(0, 0, 1))

        if isinstance(self.size, Vec3):
            trans = glm.scale(trans, glm.vec3(self.size.x, self.size.y, self.size.z))
        else:
            trans = glm.scale(trans, glm.vec3(self.size.x, self.size.y, 0.0))

        self.model = trans

        if self.texture and not self.material:
            self.texture.use(0)
        elif self.material:
           if self.material.texture:
               self.material.texture.use(0)

    def _build_vao(self):
        if self.vao and self.vbo:
            vaosvbos.remove((self.vao, self.vbo))
            self.vao.release()
            self.vbo.release()

        self.vbo, self.vao = Builder(self)
        vaosvbos.append((self.vao, self.vbo))

@ClassWrapper
class Base2D:
    def __init__(self):
        self.vao = None
        self.vbo = None
        self.texture = None
        self.position = Vec2(0.0, 0.0)
        self.size = Vec2(0.0, 0.0)
        self.dtype = DType._2D
        self.rotation = Vec1(0.0)

@ClassWrapper
class Base3D:
    def __init__(self):
        self.vao = None
        self.vbo = None
        self.texture = None
        self.position = Vec3(0.0, 0.0, 0.0)
        self.size = Vec3(0.0, 0.0, 0.0)
        self.dtype = DType._3D
        self.rotation = Vec3(0.0, 0.0, 0.0)
