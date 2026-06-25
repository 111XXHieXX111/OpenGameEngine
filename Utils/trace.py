from ..Core.modules import sys

def checkInDebbuger():
    if sys.gettrace() is not None:
        return True
    return False