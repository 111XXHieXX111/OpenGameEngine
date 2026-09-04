from ..Kernel.Components.Graphical import Color3, Color4
from ..Kernel.Components.Vectors import Vec3

class Material3D:
    def __init__(self):
        self.ambient_color = Color3(1.0, 1.0, 1.0)
        self.light_pos = Vec3(0.0, 0.0, 0.0)
        self.light_color = Color3(0.0, 0.0, 0.0)
        self.texture = None
        self.color = Color4(0.0, 0.0, 0.0, 0.0)
