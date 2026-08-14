from ..Kernel.Components.Vectors import Vec2
from ..Kernel.Kernel import ClassWrapper

@ClassWrapper
def pxtondc(coords:Vec2, window):
    winsizes = window.current_window_sizes

    ndc_x = (coords.x / winsizes.x) * 2.0 - 1.0
    ndc_y = (coords.y / winsizes.y) * 2.0 - 1.0

    return Vec2(ndc_x, -ndc_y)
