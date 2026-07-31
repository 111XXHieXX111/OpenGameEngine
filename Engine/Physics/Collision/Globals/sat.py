from ..modules import *
from .base import checkGlobalCollision
from ..sat import _SAT

@logWrapper
def _GSAT(obj, ignore:list=[]):
    return checkGlobalCollision(_SAT, obj, ignore)
