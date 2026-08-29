from ..Kernel.Kernel import GetCurrentWindow, LogWrapper
from array import array

@LogWrapper
def Builder(_self):
    window = GetCurrentWindow()
    ctx = window.window_renderer.context
    program = window.window_renderer.program
    
    data = []
    for i, v in enumerate(_self.vertices_config):
        uv = _self.uv[i]
        data.extend([v[0], v[1], v[2], uv.x, uv.y])

    vbo = ctx.buffer(array("f", data).tobytes())

    vao = ctx.vertex_array(
        program,
        [(vbo, "3f 2f", "vertex_position", "vertex_uv")]
    )

    return vbo, vao
