from ...Kernel.modules import imgui, GlfwRenderer
from ...Kernel.Components.vectors import Vec2
from ...Kernel.kernel import log_system
from .imgui_flags import GUIFlags

# RENDER&INIT

def imguiRender(impl):
    imgui.render()
    impl.render(imgui.get_draw_data())

def imguiInputs(impl):
    impl.process_inputs()
    imgui.new_frame()

def imguiInit(window):
    log_system.addInfo("Create imgui context")
    imgui.create_context()
    return GlfwRenderer(window)

# GUI

def moveANDsize(position:Vec2, size:Vec2):
    imgui.set_next_window_position(position.x, position.y, condition=imgui.ONCE)
    imgui.set_next_window_size(size.x, size.y, condition=imgui.ONCE)

## WINDOWS

def GUIBegin(title:str="Window", position:Vec2=Vec2(80, 100), size:Vec2=Vec2(300, 90), closable:bool=False, flags:GUIFlags=0):
    moveANDsize(position, size)
    return imgui.begin(title, flags=flags, closable=closable)

def GUIEnd():
    return imgui.end()

def GUIBeginChild(title:str="Window", size:Vec2=Vec2(0.0, 0.0), border:bool=True, flags:GUIFlags=0):
    return imgui.begin_child(title, width=size.x, height=size.y, border=border, flags=flags)

def GUIEndChild():
    return imgui.end_child()

## WIDGETS

def GUIText(text:str="Text"):
    return imgui.text(text)

def GUIButton(text:str="Button", size:Vec2=Vec2(0.0, 0.0)):
    return imgui.button(text, width=size.x, height=size.y)

def GUISButton(text:str="Button"):
    return imgui.small_button(text)

def GUIIButton(identifier:str="Button", size:Vec2=Vec2(800, 60), flags:GUIFlags=0):
    return imgui.invisible_button(identifier, width=size.x, height=size.y, flags=flags)

### INPUT TEXT

def GUIInputText(text:str="InputText", value:str="", buffer_length:int=0, flags:GUIFlags=0, callback:callable=None, user_data=None):
    return imgui.input_text(text, value=value, buffer_length=buffer_length, flags=flags, callback=callback, user_data=user_data)
