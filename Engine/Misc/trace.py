from ..Kernel.modules import sys
from ..Kernel.kernel import logWrapper

@logWrapper
def checkInDebugger():
    if sys.gettrace() is not None:
        return True
    return False
