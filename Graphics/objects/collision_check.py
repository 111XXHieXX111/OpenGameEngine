from .modules import *

def checkCollision(verts1:list[Vec2] | tuple[Vec2], verts2:list[Vec2] | tuple[Vec2]):
    min_x1 = min(v.x for v in verts1)
    max_x1 = max(v.x for v in verts1)
    min_y1 = min(v.y for v in verts1)
    max_y1 = max(v.y for v in verts1)
    
    min_x2 = min(v.x for v in verts2)
    max_x2 = max(v.x for v in verts2)
    min_y2 = min(v.y for v in verts2)
    max_y2 = max(v.y for v in verts2)
    
    return not (max_x1 < min_x2 or max_x2 < min_x1 or max_y1 < min_y2 or max_y2 < min_y1)