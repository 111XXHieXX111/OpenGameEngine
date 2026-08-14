from OpenGameEngine import *

window = Renderer.Window()

rect = gfx.Rectangle()

Transform.SetPosition(rect, Vec2(20, 20))
Transform.SetSize(rect, Vec2(80, 80))

@window.UpdateFunction
def Update():
    speed = 240*window.GetDelta()

    if Input.Keyboard.KeyPressed(Keys.A):
        Transform.Move(rect, Vec2(-speed, 0))
    elif Input.Keyboard.KeyPressed(Keys.D):
        Transform.Move(rect, Vec2(speed, 0))

    if Input.Keyboard.KeyPressed(Keys.W):
        Transform.Move(rect, Vec2(0, -speed))
    elif Input.Keyboard.KeyPressed(Keys.S):
        Transform.Move(rect, Vec2(0, speed))

    rect.Draw()

window.Run()