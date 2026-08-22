from ..Kernel.Components.Graphical import Color3, Color4, c3toc4
from ..Kernel.Kernel import ClassWrapper, GetCurrentWindow

@ClassWrapper
class Color:
    @staticmethod
    def Set(Object, Color:Color3 | Color4):
        Color = c3toc4(Color)
        for vertex in Object.vertices:
            vertex.r = Color.r
            vertex.g = Color.g
            vertex.b = Color.b
            vertex.a = Color.a
        Object._build_vao()

    @staticmethod
    def SetBackGround(Color:Color3 | Color4):
        GetCurrentWindow().window_renderer.fillcolor = c3toc4(Color)
