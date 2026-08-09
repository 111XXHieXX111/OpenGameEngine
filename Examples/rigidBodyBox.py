import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()
window.setStretch(stretchType.KEEP_ASPECT)

rect = gfx.Rectangle(window)
rect.setPosition(Vec2(40, 20))
rect.setSize(Vec2(80, 80))
rect.setColor(Color3(1, 0, 0))
rect.connectModule(rigidBodyBox())
rect.setModuleValue("rigidBodyBox", "velocity", Vec2(420, -40))

left_wall = gfx.Rectangle(window)
left_wall.setPosition(Vec2(0, 0))
left_wall.setSize(Vec2(20, 480))
left_wall.setColor(Color3(1, 1, 1))

right_wall = gfx.Rectangle(window)
right_wall.setPosition(Vec2(620, 0))
right_wall.setSize(Vec2(20, 480))
right_wall.setColor(Color3(1, 1, 1))

top_wall = gfx.Rectangle(window)
top_wall.setPosition(Vec2(0, 0))
top_wall.setSize(Vec2(640, 20))
top_wall.setColor(Color3(1, 1, 1))

bottom_wall = gfx.Rectangle(window)
bottom_wall.setPosition(Vec2(0, 460))
bottom_wall.setSize(Vec2(640, 20))
bottom_wall.setColor(Color3(1, 1, 1))

def update():
    global rects
    
    left_wall.drawRectangle(drawMode.FILL)
    right_wall.drawRectangle(drawMode.FILL)
    top_wall.drawRectangle(drawMode.FILL)
    bottom_wall.drawRectangle(drawMode.FILL)

    rect.drawRectangle(drawMode.FILL)

window.winProcess(update)