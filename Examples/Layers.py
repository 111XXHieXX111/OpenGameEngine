from OpenGameEngine import *

window = Renderer.Window()

player = gfx.Rectangle()
Transform.SetPosition(player, Vec2(280, 390))
Transform.SetSize(player, Vec2(80, 80))
Color.Set(player, Color3(1, 0, 0))
Layers.Set(player, 1)

rect1 = gfx.Rectangle()
Transform.SetPosition(rect1, Vec2(0, 0))
Transform.SetSize(rect1, Vec2(320, 480))
Color.Set(rect1, Color4(0, 1, 0, 0.6))
Layers.Set(rect1, 0)

rect2 = gfx.Rectangle()
Transform.SetPosition(rect2, Vec2(320, 0))
Transform.SetSize(rect2, Vec2(320, 480))
Color.Set(rect2, Color4(0, 0, 1, 0.6))
Layers.Set(rect2, 2)

@window.UpdateFunction
def Update():
    player.Draw()
    rect1.Draw()
    rect2.Draw()

window.Run()