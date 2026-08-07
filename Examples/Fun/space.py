import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from OpenGameEngine import *

window = Window()
window.initWindow()
window.setTitle("Space")
window.setSize(640, 240)

batch = batchRender(batchDrawing.STATIC)

for _ in range(800):
	star = gfx.Rectangle(window)
	star.setPosition(Vec2(
		Random.randomNum(0, 640),
		Random.randomNum(0, 240)
	))
	star.setSize(Vec2(1, 1))
	star.setColor(Color3(1, 1, 1))

	batch.addPrimitive(star)

def update():
	batch.renderPrimitives()

window.winProcess(update)