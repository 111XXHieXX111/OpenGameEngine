from .modules import os
from .kernel import log_system

log_system.addInfo("Loading icons path's")

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

icons = {
    "Icon": os.path.join(PROJECT_ROOT, "Icons", "OGE.png"),
    "HRIcon": os.path.join(PROJECT_ROOT, "Icons", "OGEHR.png"),
    "IcoIcon": os.path.join(PROJECT_ROOT, "Icons", "OGE.ico")
}