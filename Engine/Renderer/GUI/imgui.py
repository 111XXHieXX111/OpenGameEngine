from imgui.integrations.glfw import GlfwRenderer
from ...Kernel.Components.Vectors import Vec2
from ...Kernel.Kernel import log_system
from .imgui_flags import Flags
from .imgui_other import ArrowDirections
import imgui

def imguiRender(impl:GlfwRenderer):
    imgui.render()
    impl.render(imgui.get_draw_data())

def imguiInputs(impl:GlfwRenderer):
    impl.process_inputs()
    try:
        imgui.new_frame()
    except:...

def imguiInit(window):
    log_system.AddInfo("Initing imgui")
    log_system.AddDInfo("Creating imgui context")
    imgui.create_context()
    return GlfwRenderer(window)

def moveANDsize(position:Vec2, size:Vec2):
    imgui.set_next_window_position(position.x, position.y, condition=imgui.ONCE)
    imgui.set_next_window_size(size.x, size.y, condition=imgui.ONCE)

def Begin(title:str="Window", position:Vec2=Vec2(80, 100), size:Vec2=Vec2(300, 90), closable:bool=False, flags:Flags=0):
    moveANDsize(position, size)
    return imgui.begin(title, flags=flags, closable=closable)

def End():
    return imgui.end()

def BeginChild(title:str="Window", size:Vec2=Vec2(0.0, 0.0), border:bool=True, flags:Flags=0):
    return imgui.begin_child(title, width=size.x, height=size.y, border=border, flags=flags)

def EndChild():
    return imgui.end_child()

def Label(text:str="Text"):
    return imgui.text(text)

def Button(text:str="Button", size:Vec2=Vec2(0.0, 0.0)):
    return imgui.button(text, width=size.x, height=size.y)

def SmallButton(text:str="Button"):
    return imgui.small_button(text)

def InputText(text:str="InputText", value:str="", buffer_length:int=256, flags:Flags=0, callback:callable=None, user_data=None):
    return imgui.input_text(text, value=value, buffer_length=buffer_length, flags=flags, callback=callback, user_data=user_data)

def ArrowButton(text:str="Button", direction:ArrowDirections=ArrowDirections.RIGHT):
    return imgui.arrow_button(text, direction)

def InputTextMultiline(text:str="InputTextMultiline", value:str="", buffer_length:int=256, size:Vec2=Vec2(280, 120), flags:Flags=0, callback:callable=None, user_data=None):
    return imgui.input_text_multiline(text, value=value, buffer_length=buffer_length, width=size.x, height=size.y, flags=flags, callback=callback, user_data=user_data)

def SameLine(position:float=0.0, spacing:float=-1.0):
    return imgui.same_line(position=position, spacing=spacing)

def LabelUnformatted(text:str="TextUnformatted"):
    return imgui.text_unformatted(text)

def CheckBox(text:str="Checkbox", state:bool=False):
    return imgui.checkbox(text, state)

def Separator():
    return imgui.separator()

def Image(texture, size:Vec2):
    return imgui.image(texture, width=size.x, height=size.y)
