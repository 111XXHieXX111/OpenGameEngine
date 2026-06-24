from .logging import Logging
from .modules import sys, os

def colorSupportChecker():
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

log_system = Logging(True, colorSupportChecker(), True)
log_system.consoleStream(True)

log_system.addInfo("Logging system connected!")

debug = True
render_items = []

VERSION = "26.1.0.2"

log_system.addInfo(f"Open Game Engine. Version:{VERSION}")