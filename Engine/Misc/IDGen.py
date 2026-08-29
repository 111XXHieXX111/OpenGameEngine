import time

_c = 0

def IDGen():
    global _c
    _out = int(time.time()) + _c
    _c += 1
    return _out
