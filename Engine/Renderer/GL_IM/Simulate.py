from ...Kernel.Kernel import LogWrapper, log_system, paths, GetCurrentWindow
from ..Shaders.ShaderReader import ShaderReader
from ..Shaders.ShaderLoader import ShaderLoader
from array import array
import moderngl as mgl
import os

arrays = []
active_array = None
program = None

@LogWrapper
def glBegin():
    global active_array

    # Structure:
    # vertices, r, g, b, a, vao, render
    # 00000000, 1, 2, 3, 4, 555, 666666
    
    active_array = [[], 0.0, 0.0, 0.0, 1.0, None, False]
    
@LogWrapper
def glVertex2f(posx:float, posy:float):
    if active_array is None:
        raise RuntimeError("glVertex2f called without glBegin")

    r = active_array[1]
    g = active_array[2]
    b = active_array[3]
    a = active_array[4]
    active_array[0].append((posx, posy, r, g, b, a))

@LogWrapper
def glColor3f(r:float, g:float, b:float):
    if active_array is None:
        raise RuntimeError("glColor3f called without glBegin")

    active_array[1] = r
    active_array[2] = g
    active_array[3] = b

@LogWrapper
def glColor4f(r:float, g:float, b:float, a:float):
    if active_array is None:
        raise RuntimeError("glColor4f called without glBegin")

    active_array[1] = r
    active_array[2] = g
    active_array[3] = b
    active_array[4] = a

@LogWrapper
def glEnd():
    global active_array

    if active_array is None:
        raise RuntimeError("glEnd called without glBegin")
    
    active_array[6] = True

    already_exists = False
    for i, existing_array in enumerate(arrays):
        if existing_array[0] == active_array[0]:
            arrays[i][6] = active_array[6]
            already_exists = True
            break

    if not already_exists:
        arrays.append(active_array)

    active_array = None


@LogWrapper
def GL_IM_Init():
    global program
    log_system.AddDInfo("Initing GL_IM")
    vertex_shader, fragment_shader = ShaderReader(os.path.join(paths["Shaders"], "GL_IM.vert"), os.path.join(paths["Shaders"], "GL_IM.frag"))
    program = ShaderLoader(vertex_shader, fragment_shader)

@LogWrapper
def Builder():
    for _array in arrays:
        if not _array[5]:
            window = GetCurrentWindow()
            ctx = window.window_renderer.context

            data = []
            for i, v in enumerate(_array[0]):
                data.extend([v[0], v[1], v[2], v[3], v[4], v[5]])

            vbo = ctx.buffer(array("f", data).tobytes())

            vao = ctx.vertex_array(
                program,
                [(vbo, "2f 4f", "vertex_position", "vertex_color")]
            )

            _array[5] = vao

@LogWrapper
def RenderGL_IM():
    Builder()

    window = GetCurrentWindow()
    if window.camera:
        try:
            camera_matrix = window.camera._camera_matrix(window)
            program["camera_matrix"].write(camera_matrix)
        except:...

    for _array in arrays:
        if _array[5] and _array[6]:
            _array[5].render(mgl.TRIANGLE_FAN)
            _array[6] = False
