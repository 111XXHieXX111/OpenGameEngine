from .logging import Logging
from .modules import sys, os, GL, compileShader, compileProgram

def colorSupportChecker():
    log_system.addInfo(f"Platform:{sys.platform}")
    
    if not sys.stdout.isatty():
        return False
    
    if sys.platform == "win32":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            handle = kernel32.GetStdHandle(-11)
            mode = ctypes.c_ulong()
            if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
                return bool(mode.value & 0x0004)
        except:
            return False
        return False
    
    term = os.environ.get("TERM", "")
    if term == "dumb":
        return False
    
    return True

log_system = Logging(True, True, True)
log_system.consoleStream(True)

log_system.colored = colorSupportChecker()

log_system.addInfo("Logging system connected!")

debug = True
render_items = []
render_vertexes = []
textures = []
programs = []

def logWrapper(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            log_system.addWarn("KeyboardInterrupt, undo action.")
            return None
        except PermissionError:
            log_system.addError("Not enough rights!")
            return None
        except Exception as ex:
            log_system.addError(f"{ex}")
            return None
    return wrapper

def classWrapper(cls):
    for name, method in cls.__dict__.items():
        if callable(method):
            setattr(cls, name, logWrapper(method))
    return cls

shader = None

def initGFX():
    global render_type, shader

    VERTEX_SHADER_CODE = """#version 330 core

layout (location = 0) in vec3 VertexPos;
layout (location = 1) in vec3 VertexColor;
layout (location = 2) in vec2 TexCoord;

out vec3 Color;
out vec2 TexCoordOut;

void main() {
    gl_Position = vec4(VertexPos.xyz, 1.0);
    Color = VertexColor;
    TexCoordOut = TexCoord;
}"""

    FRAGMENT_SHADER_CODE = """#version 330 core

in vec3 Color;
in vec2 TexCoordOut;

uniform sampler2D textureSampler;
uniform int useTexture;

out vec4 FragColor;

void main() {
    if (useTexture == 1) {
        vec4 texColor = texture(textureSampler, TexCoordOut);
        FragColor = texColor * vec4(Color, 1.0);
    } else {
        FragColor = vec4(Color, 1.0);
    }
}"""

    log_system.addInfo("Create shaders")
    vertShader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
    GL.glShaderSource(vertShader, VERTEX_SHADER_CODE)
    fragShader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
    GL.glShaderSource(fragShader, FRAGMENT_SHADER_CODE)
    
    log_system.addInfo("Compiling shaders")
    GL.glCompileShader(vertShader)
    GL.glCompileShader(fragShader)

    log_system.addInfo("Create shader program")

    programShader = GL.glCreateProgram()

    log_system.addInfo("Attach shaders")
    GL.glAttachShader(programShader, vertShader)
    GL.glAttachShader(programShader, fragShader)

    log_system.addInfo("Link program")
    GL.glLinkProgram(programShader)

    log_system.addInfo("Delete shaders")
    GL.glDeleteShader(vertShader)
    GL.glDeleteShader(fragShader)
    
    log_system.addInfo("Set render type to 0")
    render_type = 0
    
    programs.append(programShader)

    shader = programShader

def getShader():
    return shader
