from .logging import Logging
from .modules import pyfiglet

print(pyfiglet.figlet_format("Open Game Engine"))

log_system = Logging(True, True, True)
log_system.consoleStream(True)

log_system.addInfo("Logging system connected!")

debug = True
render_items = []