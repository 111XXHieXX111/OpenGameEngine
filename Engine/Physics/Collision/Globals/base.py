from ....Kernel.kernel import render_items
from ....Graphics.Primitives.rectangle import Rectangle
from ....Graphics.Primitives.triangle import Triangle
from ....Graphics.Primitives.circle import Circle
from ..modules import *

@logWrapper
def checkGlobalCollision(collision_function, obj, ignore:list=[]):
    colliding = False
    for item in render_items:
        if item == obj:
            continue

        if item in ignore:
            continue

        if isinstance(item, Rectangle) or isinstance(item, Triangle) or isinstance(item, Circle):
            if collision_function(item.vertexes, obj.vertexes):
                colliding = True
                break

    return colliding
