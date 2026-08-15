from ...Kernel.Kernel import log_system, ClassWrapper, SetCurrentWindow, render_items
from ...Kernel.Memory import ReleaseTextures, ReleaseShaders
from ...Kernel.Components.Vectors import Vec2
from ...Input.Keyboard import _Keyboard
from ..GUI.imgui import imguiInit, imguiInputs, imguiRender
from ..GUI.Window.InfoMonitor import InfoMonitor
from ..Camera.Camera2D import Camera2D
from .WindowRenderer import WindowRenderer
from .WindowOther import FPSCounter, DeltaCounter
import glfw

@ClassWrapper
class Window:
    def __init__(self):
        log_system.AddInfo("Initializing the window")

        self.update_function = None
        self.to_render = []
        self.current_window_sizes = Vec2(0.0, 0.0)
        self.key_callbacks = [(glfw.KEY_F12, self._f12_callback)]
        self.info_monitor_render = False
        self.camera = None

        self.window_settings = {
            "WindowSize":[640, 480],
            "WindowTitle":"Window"
        }

        log_system.AddDInfo("Initing glfw")
        if not glfw.init():
            log_system.AddCritical("Glfw not inited")
            quit(-1)

        log_system.AddDInfo("Creating window")
        self.window = glfw.create_window(self.window_settings["WindowSize"][0], self.window_settings["WindowSize"][1], "Window", None, None)

        log_system.AddDInfo("Checking window")
        if not self.window:
            log_system.AddCritical("Error creating window")
            glfw.terminate()
            quit(-1)
        
        log_system.AddDInfo("Making current context")
        glfw.make_context_current(self.window)

        log_system.AddDInfo("Creating WindowRenderer")
        self.window_renderer = WindowRenderer(self)

        log_system.AddDInfo("Setting current window")
        SetCurrentWindow(self)

        log_system.AddDInfo("Loading base shader")
        self.window_renderer.LoadBaseShader()

        self.impl = imguiInit(self.window)

        log_system.AddDInfo("Creating InfoMonitor")
        self.infomonitor = InfoMonitor(self)

        log_system.AddDInfo("Creating FPSCounter")
        self.fpscounter = FPSCounter(self)

        log_system.AddDInfo("Creating DeltaCounter")
        self.deltacounter = DeltaCounter(self)

        log_system.AddDInfo("Getting current window sizes")
        winsize = glfw.get_framebuffer_size(self.window)
        self.current_window_sizes = Vec2(winsize[0], winsize[1])

        log_system.AddDInfo("Connecting callbacks")

        glfw.set_key_callback(self.window, self._key_callback)

        log_system.AddDInfo("Getting primary monitor")

        try:
            log_system.AddInfo(f"OpenGL Version:{self.window_renderer.context.version_code}")
            log_system.AddInfo(f"GLSL Version:{self.window_renderer.context.info['GL_VERSION']}")
            log_system.AddDInfo(f"Render:{self.window_renderer.context.info['GL_RENDERER']}")
        except Exception as ex:
            log_system.AddWarn(f"Information could not be retrieved:{ex}")

        try:
            monitor = glfw.get_primary_monitor()
            mode = glfw.get_video_mode(monitor)
            resolution = mode.size

            log_system.AddDInfo(f"Selected monitor:{glfw.get_monitor_name(monitor).decode("utf-8")}")
            log_system.AddDInfo(f"Resolution:{resolution.width}x{resolution.height}, {mode.refresh_rate}GHz")

            del mode, resolution, monitor
        except Exception as ex:
            log_system.AddDWarn(f"Information could not be retrieved:{ex}")

    def SetSize(self, Size:Vec2):
        log_system.AddDInfo(f"Setting window size:{Size.x}x{Size.y}")
        glfw.set_window_size(self.window, Size.x, Size.y)
        self.window_settings["WindowSize"] = [Size.x, Size.y]

    def SetTitle(self, Title:str):
        log_system.AddDInfo(f"Setting window title:{Title}")
        glfw.set_window_title(self.window, Title)
        self.window_settings["WindowTitle"] = Title

    def GetFPS(self):
        return self.fpscounter.fps

    def GetDelta(self):
        return self.deltacounter.delta

    def SetVSync(self, sync:int):
        log_system.AddDInfo(f"VSync:{bool(sync)}")
        glfw.swap_interval(sync)

    def SetCamera(self, camera:Camera2D):
        self.camera = camera

    def _f12_callback(self):
        if _Keyboard.KeyJustPressed(glfw.KEY_F12):
            if _Keyboard.KeyPressed(glfw.KEY_LEFT_SHIFT):
                return
        
            self.info_monitor_render = not self.info_monitor_render

    def _key_callback(self, window, key, scancode, action, mods):
        for callback in self.key_callbacks:
            if callback[0] == key:
                callback[1]()

    def Run(self):
        while not glfw.window_should_close(self.window):
            render_items.clear()

            winsize = glfw.get_framebuffer_size(self.window)
            self.current_window_sizes = Vec2(winsize[0], winsize[1])

            if self.current_window_sizes.x <= 0 or self.current_window_sizes.y <= 0:
                glfw.poll_events()
                continue
            
            self.window_renderer.Renderer()

            imguiInputs(self.impl)

            if self.update_function:
                self.update_function()
            
            if self.info_monitor_render:
                self.infomonitor.Render()

            imguiRender(self.impl)

            self.fpscounter.FPSCalculate()
            self.deltacounter.DeltaCalculate()

            glfw.poll_events()
            glfw.swap_buffers(self.window)

        print(self.to_render)
        log_system.AddDInfo("Terminate glfw")
        glfw.terminate()
        ReleaseTextures()
        ReleaseShaders()

    def UpdateFunction(self, func):
        log_system.AddDInfo("Set update function")
        self.update_function = func
