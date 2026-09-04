from ..Renderer.Material import Material3D

class Material:
    @staticmethod
    def Set(Object, Material:Material3D):
        Object.material = Material
        Object._build_vao()
