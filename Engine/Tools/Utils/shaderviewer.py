from Engine.Graphics.Window.glfw_window import Window
from Engine.Kernel.Components.vectors import Vec2
from Engine.Kernel.Components.graphics import Color3, drawMode, stretchType
from Engine.Graphics.Primitives.rectangle import Rectangle
from Engine.Misc.frametimer import frameTimer
from Engine.Graphics.Utils.shader import loadShader

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