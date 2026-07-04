from ..Kernel.modules import sys
from ..Kernel.kernel import logWrapper

@logWrapper
def checkInDebbuger():
    if sys.gettrace() is not None:
        return True
    return False
