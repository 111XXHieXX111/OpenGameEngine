from ..Kernel.modules import time

_counter = -1

def generateID():
    _counter += 1
    return int(time.time()) + _counter
