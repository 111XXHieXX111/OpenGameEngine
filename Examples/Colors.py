from OpenGameEngine import *

window = Renderer.Window()

rect = gfx.Rectangle()

Transform.SetPosition(rect, Vec2(20, 20))
Transform.SetSize(rect, Vec2(80, 80))

Color.Set(rect, Color3(1, 0, 0))

@window.UpdateFunction
def Update():
    rect.Draw()

window.Run()