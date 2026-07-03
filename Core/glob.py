from .logging import Logging
from .modules import sys, os
from OpenGL.GLUT import GLUT_BITMAP_HELVETICA_10, GLUT_BITMAP_HELVETICA_12, GLUT_BITMAP_HELVETICA_18, GLUT_BITMAP_TIMES_ROMAN_10, GLUT_BITMAP_TIMES_ROMAN_24 # type: ignore

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
textures = []

log_system.addInfo("Loading icons path's")

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

icons = {
    "Icon": os.path.join(PROJECT_ROOT, "Icons", "OGE.png"),
    "HRIcon": os.path.join(PROJECT_ROOT, "Icons", "OGEHR.png"),
    "IcoIcon": os.path.join(PROJECT_ROOT, "Icons", "OGE.ico")
}

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

log_system.addInfo("Loading OpenGL fonts")

fonts = {
    "HELVETICA 10":GLUT_BITMAP_HELVETICA_10,
    "HELVETICA 12":GLUT_BITMAP_HELVETICA_12,
    "HELVETICA 18":GLUT_BITMAP_HELVETICA_18,
    "ROMAN 10":GLUT_BITMAP_TIMES_ROMAN_10,
    "ROMAN 24":GLUT_BITMAP_TIMES_ROMAN_24
}