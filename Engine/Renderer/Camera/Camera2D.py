from ...Kernel.Components.Vectors import Vec2
from ..Utils import pxtondc
import glm

class Camera2D:
    def __init__(self):
        self.position = Vec2(0.0, 0.0)
        self.zoom = 2.0

    def _camera_matrix(self, window):
        pos = pxtondc(self.position, window)

        matrix = glm.mat4(
            glm.vec4(2/self.zoom, 0, 0, 0),
            glm.vec4(0, 2/self.zoom, 0, 0),
            glm.vec4(0, 0, 1, 0),
            glm.vec4(-pos.x, -pos.y, 0, 1)
        )

        return matrix
