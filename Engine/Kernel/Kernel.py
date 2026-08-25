from .Logging import Logging
import traceback
import os

log_system = Logging()
log_system.ConsoleStream(True)

os.system("")

current_window = None
engine_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
opengine_folder = os.path.dirname(engine_folder)
render_items = []
textures = []
shaders = []
vaosvbos = []

paths = {
    "Shaders":os.path.join(engine_folder, "Shaders")
}

textures_path = os.path.join(opengine_folder, "Textures")

def LogWrapper(func):
    def Wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            log_system.AddWarn("KeyboardInterrupt, undo action.")
            return Wrapper(*args, **kwargs)
        except PermissionError:
            log_system.AddError("Not enough rights!")
            return None
        except Exception as ex:
            error_info = traceback.format_exc()
            log_system.AddError(f"Error: {error_info}")
            return None
    return Wrapper

def ClassWrapper(cls):
    for name, method in cls.__dict__.items():
        if callable(method):
            setattr(cls, name, LogWrapper(method))
    return cls

def SetCurrentWindow(Window):
    global current_window
    current_window = Window

def GetCurrentWindow():
    return current_window
