import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()
window.setBG(Color3(0.1, 0.1, 0.1))
window.setTitle("Primitives")
window.setStretch(stretchType.KEEP_ASPECT)

rect = Graphics.Rectangle(window)
rect.setPosition(Vec2(45, 60))
rect.setSize(Vec2(70, 70))
rect.setColor(Color3(0, 0, 1))

tri = Graphics.Triangle(window)
tri.setPosition(Vec2(320, 150))
tri.setSize(Vec2(100, 90))
tri.setColor(Color3(1, 0, 0))

circle = Graphics.Circle(32, window)
circle.setPosition(Vec2(520, 180))
circle.setSize(Vec2(110, 110))
circle.setColor(Color3(0, 1, 0))

line = Graphics.Line(window)
line.setPoint1(Vec2(80, 380))
line.setPoint2(Vec2(450, 320))
line.setColor(Color3(0.5, 0, 1))
line.setWidthLines(Vec1(2))

def update():
	rect.drawRectangle(drawMode.FILL)
	tri.drawTriangle(drawMode.FILL)
	circle.drawCircle(drawMode.FILL)
	line.drawLine()

window.winProcess(update)