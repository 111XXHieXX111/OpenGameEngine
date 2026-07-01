import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

parent_dir = os.path.dirname(project_root)
sys.path.insert(0, parent_dir)

from OpenGameEngine.Graphics.window.window import Window # type: ignore
from OpenGameEngine.Core.base import Vec2, Color3, drawMode, stretchType # type: ignore
from OpenGameEngine.Graphics import Rectangle # type: ignore
from OpenGameEngine.Utils.General.frametimer import frameTimer # type: ignore
from OpenGameEngine.Utils.General.shader import loadShader # type: ignore

selected = "r"
file_path = ""
shader = None

window = Window()
window.initWindow()
window.setTitle("OShaderIDE")
window.setSize(int(640//1.5), int(480//1.5))
window.setStretch(stretchType.EXPAND)

rect = Rectangle(window)
rect.setColor(Color3(1, 1, 1))

def load_shader():
    global shader
    
    from .manager import file_path
    
    if file_path:
        shader = loadShader(file_path)

update_timer = frameTimer(20, load_shader)

def draw():
    rect.setSize(Vec2(window.current_window_sizes[0], window.current_window_sizes[1]))
    rect.setShader(shader)
    rect.calculateSize()
    rect.drawRectangle(drawMode.FILL)
    update_timer.timerProcess()
    window.drawText("Shader preview")

window.winProcess(draw, 20)