from .modules import *

@logWrapper
def _SAT(verts1:list[Vec2] | tuple[Vec2], verts2:list[Vec2] | tuple[Vec2]):
    axes = []
    
    for i in range(len(verts1)):
        v1 = verts1[i]
        v2 = verts1[(i + 1) % len(verts1)]
        edge = Vec2(v2.x - v1.x, v2.y - v1.y)
        normal = Vec2(-edge.y, edge.x)
        length = (normal.x ** 2 + normal.y ** 2) ** 0.5
        if length != 0:
            normal = Vec2(normal.x / length, normal.y / length)
        axes.append(normal)
    
    for i in range(len(verts2)):
        v1 = verts2[i]
        v2 = verts2[(i + 1) % len(verts2)]
        edge = Vec2(v2.x - v1.x, v2.y - v1.y)
        normal = Vec2(-edge.y, edge.x)
        length = (normal.x ** 2 + normal.y ** 2) ** 0.5
        if length != 0:
            normal = Vec2(normal.x / length, normal.y / length)
        axes.append(normal)
    
    for axis in axes:
        min1 = max1 = verts1[0].x * axis.x + verts1[0].y * axis.y
        for v in verts1[1:]:
            proj = v.x * axis.x + v.y * axis.y
            if proj < min1: min1 = proj
            if proj > max1: max1 = proj
        
        min2 = max2 = verts2[0].x * axis.x + verts2[0].y * axis.y
        for v in verts2[1:]:
            proj = v.x * axis.x + v.y * axis.y
            if proj < min2: min2 = proj
            if proj > max2: max2 = proj
        
        if max1 < min2 or max2 < min1:
            return False
    
    return True
