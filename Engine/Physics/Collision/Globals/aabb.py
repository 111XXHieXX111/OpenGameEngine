from ..modules import *
from .base import checkGlobalCollision
from ..aabb import _AABB

@logWrapper
def _GAABB(obj, ignore:list=[]):
    return checkGlobalCollision(_AABB, obj, ignore)
