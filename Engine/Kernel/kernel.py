from .logging import Logging
from .modules import sys, os, GL, compileShader, compileProgram, traceback

# OLD (NOT USING)

def colorSupportChecker():
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

# LOGGING:

log_system = Logging()
log_system.consoleStream(True)

os.system("")

log_system.addInfo("Logging system connected!")

log_system.addDInfo(f"Platform:{sys.platform}")

# OTHER

debug = True
render_items = []
render_vertexes = []
textures = []
programs = []

def setDebug(dbg:bool):
    global debug
    debug = dbg
    log_system.consoleStream(dbg)

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
            error_info = traceback.format_exc()
            log_system.addError(f"Error: {error_info}")
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

    log_system.addInfo("Init GFX")

    try:
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

        log_system.addDInfo("Create shaders")
        vertShader = GL.glCreateShader(GL.GL_VERTEX_SHADER)
        GL.glShaderSource(vertShader, VERTEX_SHADER_CODE)
        fragShader = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)
        GL.glShaderSource(fragShader, FRAGMENT_SHADER_CODE)
    
        log_system.addDInfo("Compiling shaders")
        GL.glCompileShader(vertShader)
        GL.glCompileShader(fragShader)

        log_system.addDInfo("Create shader program")

        programShader = GL.glCreateProgram()

        log_system.addDInfo("Attach shaders")
        GL.glAttachShader(programShader, vertShader)
        GL.glAttachShader(programShader, fragShader)

        log_system.addDInfo("Link program")
        GL.glLinkProgram(programShader)

        log_system.addDInfo("Delete shaders")
        GL.glDeleteShader(vertShader)
        GL.glDeleteShader(fragShader)
    
        log_system.addDInfo("Set render type to 0")
        render_type = 0
    
        programs.append(programShader)

        shader = programShader
    except Exception as ex:
        log_system.addCritical(f"Error compiling shader:{ex}, use render mode 0!")
        quit(1)

@logWrapper
def getShader():
    return shader
