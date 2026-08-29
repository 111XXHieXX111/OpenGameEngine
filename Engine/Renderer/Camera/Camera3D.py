from ...Kernel.Components.Vectors import Vec3
import glm
import math

class Camera3D:
    def __init__(self):
        self.model = glm.mat4(1)
        self.view = glm.mat4(1)
        self.proj = glm.mat4(1)
        self.fov = 75.0
        self.position = Vec3(0.0, 0.0, 0.0)
        self.pitch = 0.0
        self.yaw = 0.0
    
    def _calculate(self, window):
        direction = glm.vec3()
        direction.x = math.cos(glm.radians(self.yaw)) * math.cos(glm.radians(self.pitch))
        direction.y = math.sin(glm.radians(self.pitch))
        direction.z = math.sin(glm.radians(self.yaw)) * math.cos(glm.radians(self.pitch))
        camera_front = glm.normalize(direction)

        glm_pos = glm.vec3(self.position.x, self.position.y, self.position.z)

        self.view = glm.lookAt(glm_pos, glm_pos + camera_front, glm.vec3(0.0, 1.0, 0.0)); 

        winsize = window.current_window_sizes
        
        self.proj = glm.perspective(glm.radians(self.fov), winsize.x / winsize.y, 0.1, 100.0)

    def _get(self, window):
        self._calculate(window)
        return self.view, self.proj
