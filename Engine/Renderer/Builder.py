from ..Kernel.Kernel import GetCurrentWindow, LogWrapper, log_system
from array import array

@LogWrapper
def Builder(_self):
    window = GetCurrentWindow()
    ctx = window.window_renderer.context
    program = window.window_renderer.program
    material = window.window_renderer.material
    
    data = []
    for i, v in enumerate(_self.vertices_config):
        uv = _self.uv[i]
        normal = _self.normals[i]
        data.extend([v[0], v[1], v[2], uv.x, uv.y, normal[0], normal[1], normal[2]])

    vbo = ctx.buffer(array("f", data).tobytes())

    if _self.material and material:
        vao = ctx.vertex_array(
            material,
            [(vbo, "3f 2f 3f", "vertex_position", "vertex_uv", "vertex_normal")]
        )
    else:
        if _self.material:
            log_system.AddDWarn(f"Material is don't using! Using BaseColor shader. Object ID:{_self.id}")

        vao = ctx.vertex_array(
            program,
            [(vbo, "3f 2f 12x", "vertex_position", "vertex_uv")]
        )

    return vbo, vao
