from turtle import color
from OpenGameEngine import *

window = Renderer.Window()

color_index = 0
colors = (
    Color3(1, 0, 0),
    Color3(0, 1, 0),
    Color3(0, 0, 1)
)

rect = gfx.Rectangle()

Transform.SetPosition(rect, Vec2(20, 20))
Transform.SetSize(rect, Vec2(80, 80))

Color.Set(rect, Color3(1, 0, 0))

def ChangeColor():
    global color_index
    Color.Set(rect, colors[color_index])
    color_index += 1

    if color_index >= len(colors):
        color_index = 0

color_timer = Misc.Timer(0.4, ChangeColor)

@window.UpdateFunction
def Update():
    color_timer.Process()
    rect.Draw()

window.Run()