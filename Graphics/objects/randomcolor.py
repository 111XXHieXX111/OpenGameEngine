from ...Core.modules import random
from ...Core.base import Color3, Color4
from ...Core.glob import logWrapper

@logWrapper
def randomColor3():
    r = random.uniform(0.000, 1.000)
    g = random.uniform(0.000, 1.000)
    b = random.uniform(0.000, 1.000)
    
    return Color3(r, g, b)

@logWrapper
def randomColor4(random_alpha=False):
    r = random.uniform(0.000, 1.000)
    g = random.uniform(0.000, 1.000)
    b = random.uniform(0.000, 1.000)
    if random_alpha:
        a = random.uniform(0.000, 1.000)
    else:
        a = 1.0
    return Color4(r, g, b, a)
