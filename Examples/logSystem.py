import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

log_system.addInfo("Info")
log_system.addWarn("Warn")
log_system.addError("Error")
log_system.addCritical("Critical")
