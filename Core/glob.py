from .logging import Logging

log_system = Logging(True, True, True)
log_system.consoleStream(True)

log_system.addInfo("Logging system connected!")

debug = True
render_items = []