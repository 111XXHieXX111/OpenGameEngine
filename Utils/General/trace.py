from ...Core.modules import sys
from ...Core.glob import logWrapper

@logWrapper
def checkInDebbuger():
    if sys.gettrace() is not None:
        return True
    return False
