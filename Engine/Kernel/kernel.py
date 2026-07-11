from .logging import Logging
from .modules import sys, os

def colorSupportChecker():
    log_system.addInfo(f"Platform:{sys.platform}")
    
    if not sys.stdout.isatty():
        return False
    
    if sys.platform == "win32":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)
            mode = ctypes.c_ulong()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                return bool(mode.value & 0x0004)
        except:
            return False
        return False
    
    term = os.environ.get("TERM", "")
    if term == "dumb":
        return False
    
    return True

log_system = Logging(True, True, True)
log_system.consoleStream(True)

log_system.colored = colorSupportChecker()

log_system.addInfo("Logging system connected!")

debug = True
render_items = []
render_vertexes = []
textures = []

def logWrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            log_system.addWarn("KeyboardInterrupt, undo action.")
            return None
        except PermissionError:
            log_system.addError("Not enough rights!")
            return None
        except Exception as ex:
            log_system.addError(f"{ex}")
            return None
    return wrapper

def classWrapper(cls):
    for name, method in cls.__dict__.items():
        if callable(method):
            setattr(cls, name, logWrapper(method))
    return cls
