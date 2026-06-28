import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()
window.setBG(Color3(1, 1, 1))

def test_func():
    print("Hello, World!")

window.addElement(
    SimpleButton("Hello, World!", Vec2(20, 20), Vec2(120, 60), Color3(0, 0, 0), test_func) # arg1 - text, arg2 - position, arg3 - size, arg4 - text color (fg), arg5 - function (optional)
)

window.winProcess(fps=60)