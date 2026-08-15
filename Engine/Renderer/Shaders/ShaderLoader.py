from ...Kernel.Kernel import GetCurrentWindow, log_system, LogWrapper, shaders

@LogWrapper
def ShaderLoader(vertex_shader:str, fragment_shader:str):
    window = GetCurrentWindow()

    context = window.window_renderer.context

    log_system.AddInfo("Creating shader program")

    program = context.program(vertex_shader, fragment_shader)

    shaders.append(program)

    return program
