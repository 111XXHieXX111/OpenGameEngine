from ..Kernel.Kernel import GetCurrentWindow, LogWrapper
from array import array

@LogWrapper
def Builder(vertices):
    window = GetCurrentWindow()
    ctx = window.window_renderer.context
    program = window.window_renderer.program

    data = []
    for v in vertices:
        data.extend([v.x, v.y, v.z, v.r, v.g, v.b, v.a, v.u, v.v])

    vbo = ctx.buffer(array("f", data).tobytes())

    vao = ctx.vertex_array(
        program,
        [(vbo, "3f 4f 2f", "vertex_position", "vertex_color", "vertex_uv")]
    )

    return vbo, vao
