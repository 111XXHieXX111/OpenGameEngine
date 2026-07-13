import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window(0)
window.initWindow()

def test():
    print("Hello!")

window.addElement(
    SimpleButton("Button", Vec2(0, 30), Vec2(120, 40), Color3(1, 1, 1), test, fonts["HELVETICA 12"])
)

window.addElement(
    textInput(Vec2(0, 75), Vec2(120, 40), Color3(1, 1, 1), fonts["HELVETICA 12"])
)

def update():
    window.drawText("Text", Vec2(0, 10), font=fonts["ROMAN 24"])

window.winProcess(update, 60)