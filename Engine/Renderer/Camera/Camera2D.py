from ...Kernel.Components.Vectors import Vec2
import glm

class Camera2D:
    def __init__(self):
        self.position = Vec2(0.0, 0.0)
        self.zoom = 1.0

    def _camera_matrix(self, window):
        winsize = window.current_window_sizes

        # Old matrix
        # Don't use it

        # matrix = glm.mat4(
        #     glm.vec4(2/self.zoom, 0, 0, 0),
        #     glm.vec4(0, 2/self.zoom, 0, 0),
        #     glm.vec4(0, 0, 1, 0),
        #     glm.vec4(-pos.x, -pos.y, 0, 1)
        # )

        matrix = glm.ortho(0, winsize.x, winsize.y, 0.0, -1.0, 1.0)

        matrix *= glm.translate(glm.mat4(1.0), glm.vec3(-self.position.x, -self.position.y, 0.0))

        matrix = glm.scale(matrix, glm.vec3(self.zoom, self.zoom, 1.0))

        return matrix
