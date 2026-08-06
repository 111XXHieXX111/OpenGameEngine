import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()

rect = gfx.Rectangle(window)
rect.setPosition(Vec2(280, 200))
rect.setSize(Vec2(80, 80))
rect.setColor(Color3(1, 0, 0))

def update():
    if rect.isPressed(MouseButton.LEFT):
        rect.setColor(Color3(0, 0, 1))
    elif rect.isHovered:
        rect.setColor(Color3(0, 1, 0))
    else:
        rect.setColor(Color3(1, 0, 0))

    rect.drawRectangle(drawMode.FILL)

window.winProcess(update)