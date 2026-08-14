from OpenGameEngine import *

window = Renderer.Window()

rect = gfx.Rectangle()
tri = gfx.Triangle()

Transform.SetPosition(rect, Vec2(20, 20))
Transform.SetSize(rect, Vec2(80, 80))

Transform.SetPosition(tri, Vec2(120, 20))
Transform.SetSize(tri, Vec2(80, 80))

@window.UpdateFunction
def Update():
    rect.Draw()
    tri.Draw()

window.Run()