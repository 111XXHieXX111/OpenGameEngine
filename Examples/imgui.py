import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()

def update():
    GUIBegin("Test", flags=GUIFlags.WINDOW_ALWAYS_VERTICAL_SCROLLBAR)
    
    GUIText("Test")
    
    GUIBeginChild("TestChild", Vec2(200, 80))
    GUIText("Test text in child")
    GUIEndChild()

    GUIButton()
    GUISButton()
    GUIIButton()
    
    GUIInputText()

    GUIEnd()

window.winProcess(update)