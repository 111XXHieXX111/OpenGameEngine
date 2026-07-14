from ...Kernel.modules import glfw, GL, time, glutInit, threading
from ...Kernel.kernel import log_system, debug, render_items, classWrapper, render_vertexes, initGFX
from ...Kernel.Components.vectors import Vec2
from ...Kernel.Components.control import Key
from ...Kernel.Components.graphics import Color3, Color4, stretchType
from ...Kernel.Components.system import System
from ...Kernel.fonts import fonts
from ...Misc.memory import memoryMonitor, memoryClean
from ...Misc.timer import Timer
from ...Control.keyboard import Keyboard
from ...Control.mouse import Mouse
from ..GUI.window import _drawText, SimpleButton, textInput, _drawTextBox

@classWrapper
class Window:
    def __init__(self, render_type=1):

        # CHECK INIT

        log_system.addInfo("Check init")

        if not glfw.init():
            return

        # WINDOW SETTINGS

        log_system.addInfo("Create winsettings")

        self.window_settings = {
            "title":"Window",
            "width":640,
            "height":480,
            "stretch":stretchType.RELATIVELY
        }
        
        self.elements = []

        self.frame_count = 0
        self.fps = 0
        self.last_fps_time = time.time()
        
        self.delta_time = 0.0
        self.last_frame_time = time.time()
        
        self.iconified = 0
        self.iconifiedwork = True
        
        self.debugmenu = 0
        
        self.selected_keyboard = None
        
        self.upd_fps_timer = Timer(1, self._set_upd_fps)
        self.upd_fps = 0

        self.render_type = render_type

        # CURRENT SIZES

        log_system.addInfo("Create current win sizes")

        self.current_window_sizes = [640, 480]
        
        # CAMERA
        
        self.camera = {
            "x":0.0,
            "y":0.0,
            "zoom":1.0,
            "enabled":False
        }

    def _on_close_callback(self, window):
        memoryClean()

    def _iconify_callback(self, window, iconified):
        self.iconified = iconified

    def _set_upd_fps(self):
        self.upd_fps = self.fps

    def initWindow(self):
        log_system.addInfo("Init window")
        
        # CREATE WINDOW

        log_system.addInfo("Creating window")
        
        self.window = glfw.create_window(
            self.window_settings.get("width"),
            self.window_settings.get("height"),
            self.window_settings.get("title"),
            None,
            None
        )

        if not self.window:
            glfw.terminate()
            return

        # INIT GLUT
        
        log_system.addInfo("Glut init")
        
        glutInit()
        
        # INIT MEMORY MANAGER
        
        log_system.addInfo("Memory manager init")
        
        self.memorymonitor = memoryMonitor()

        # MOVE WINDOW TO THE CURRENT CONTEXT

        log_system.addInfo("Move window to the current context")
        
        glfw.make_context_current(self.window)
        
        # INFO
        
        try:
            log_system.addInfo(f"OpenGL Version:{GL.glGetString(GL.GL_VERSION).decode()}")
            log_system.addInfo(f"GLSL Version:{GL.glGetString(GL.GL_SHADING_LANGUAGE_VERSION).decode()}")
            log_system.addInfo(f"Render:{GL.glGetString(GL.GL_RENDERER).decode()}")
        except Exception as ex:
            log_system.addError(f"Information could not be retrieved:{ex}")
        
        # GFX INIT

        if self.render_type == 0:
            log_system.addInfo(f"Init GFX ({self.render_type}) (experemental)")
            initGFX()

        # VSYNC

        glfw.swap_interval(0)

        # GET CURRENT WINDOW SIZES

        log_system.addInfo("Get current win sizes")

        self.current_window_sizes = glfw.get_framebuffer_size(self.window)
        
        # CONNECT CALLBACK(S)
        
        log_system.addInfo("Connect callback(s)")
        
        glfw.set_window_iconify_callback(self.window, self._iconify_callback)
        glfw.set_window_close_callback(self.window, self._on_close_callback)

    def setStretch(self, stretch:stretchType):
        log_system.addInfo("Setting stretch")
    
        # APPLY STRETCH
        
        self.window_settings["stretch"] = stretch
    
    def getFPS(self):
        return self.fps

    def getDelta(self):
        return self.delta_time

    def setTitle(self, title:str="Window"):
        log_system.addInfo("Set title")
        
        # CHECK TYPE
        
        if not isinstance(title, str):
            log_system.addError("Use string in setTitle")
            return

        # CHECK EMPTY

        if System.check_empty(title):
            return

        # APPLY TITLE
        
        self.window_settings["title"] = title

        glfw.set_window_title(
            self.window, 
            self.window_settings.get("title")
        )
    
    def setSize(self, width:int=640, height:int=480):
        log_system.addInfo("Set size")
        
        # CHECK TYPES
        
        if not isinstance(width, int) or not isinstance(height, int):
            log_system.addError("Use int in setSize")
            return

        # APPLY SIZE

        self.window_settings["width"] = width
        self.window_settings["height"] = height

        glfw.set_window_size(
            self.window, 
            self.window_settings["width"], 
            self.window_settings["height"]
        )

    def setBG(self, color:Color3 | Color4):
        c = color
        
        # CHECK TYPE
        
        if isinstance(color, tuple) or isinstance(color, list):
            log_system.addWarn("Use Color3|Color4 for setBG")
            c = Color3(color[0], color[1], color[2])
        else:
            if not isinstance(color, Color3) and not isinstance(color, Color4):
                log_system.addError("Use Color3|Color4 for setBG")
                return
        
        log_system.addInfo(f"Set BG: ({c.r}, {c.g}, {c.b})")
        
        # SET COLOR AND CONVERT
        
        self.color = c
        self.color = System.c3toc4(self.color)
        
        # SETUP COLOR
                
        GL.glClearColor(self.color.r, self.color.g, self.color.b, self.color.a)

    def enableEventsByIconify(self):
        log_system.addInfo("Iconified work:Enabled")
        self.iconifiedwork = True
    
    def disableEventsByIconify(self):
        log_system.addInfo("Iconified work:Disabled")
        self.iconifiedwork = False

    def drawText(self, text:str, position:Vec2=Vec2(0.0, 0.0), color:Color3=Color3(1.0, 0.0, 0.0), font=fonts["HELVETICA 12"], static_text=True, *, debug_only=False):
        _drawText(self, text, position, color, font, debug_only, False, static_text)
    
    def drawTextBox(self, text:str, position:Vec2=Vec2(0.0, 0.0), charslen:int=0, color:Color3=Color3(1.0, 0.0, 0.0), bgcolor:Color4=Color4(0.0, 0.0, 0.0, 0.0), static_text=True, *, debug_only=False):
        _drawTextBox(self, text, position, color, charslen, bgcolor, debug_only, False, False, static_text)
    
    def addElement(self, element:SimpleButton | textInput):
        self.elements.append(element)
    
    def removeElement(self, element:SimpleButton | textInput):
        self.elements.remove(element)
    
    def setCameraPosition(self, position:Vec2):
        self.camera["x"] = position.x
        self.camera["y"] = position.y
    
    def moveCamera(self, move:Vec2):
        self.camera["x"] += move.x
        self.camera["y"] += move.y
    
    def setCameraZoom(self, zoom:float):
        self.camera["zoom"] = zoom
    
    def getCameraPosition(self):
        return Vec2(self.camera["x"], self.camera["y"])
    
    def setCameraEnabled(self, enabled:bool):
        self.camera["enabled"] = enabled
    
    def _render_frame(self, update=None):
        
        # GET CURRENT WINDOW SIZES

        self.current_window_sizes = list(glfw.get_framebuffer_size(self.window))
        
        # DELTA
        
        current_time = time.time()
        self.delta_time = current_time - self.last_frame_time
        self.last_frame_time = current_time
        
        if self.delta_time > 0.05:
            self.delta_time = 0.05
        
        # SKIP RENDER
        
        if self.current_window_sizes[0] <= 0 or self.current_window_sizes[1] <= 0:
            glfw.poll_events()
            return
        
        # CLEAR RENDER ITEMS
        
        render_items.clear()
        
        # CLEAR VERTEXES
        
        render_vertexes.clear()

        # CLEAR SCREEN

        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        # VIEWING AREA

        if self.window_settings["stretch"] == stretchType.KEEP_ASPECT:
            scale = min(self.current_window_sizes[0] / self.window_settings["width"], self.current_window_sizes[1] / self.window_settings["height"])
            new_w = int(self.window_settings["width"] * scale)
            new_h = int(self.window_settings["height"] * scale)
            offset_x = (self.current_window_sizes[0] - new_w) // 2
            offset_y = (self.current_window_sizes[1] - new_h) // 2
            GL.glViewport(offset_x, offset_y, new_w, new_h)
        else:
            GL.glViewport(0, 0, self.current_window_sizes[0], self.current_window_sizes[1])

        # PROJECTION MATRIX

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        
        if self.window_settings["stretch"] == stretchType.KEEP_ASPECT:
            GL.glOrtho(0, self.window_settings["width"], self.window_settings["height"], 0, -1, 1)
        else:
            GL.glOrtho(0, self.current_window_sizes[0], self.current_window_sizes[1], 0, -1, 1)

        # CAMERA

        if self.camera["enabled"]:
            width = self.window_settings["width"] if self.window_settings["stretch"] == stretchType.KEEP_ASPECT else self.current_window_sizes[0]
            height = self.window_settings["height"] if self.window_settings["stretch"] == stretchType.KEEP_ASPECT else self.current_window_sizes[1]
            
            GL.glScalef(1.0 / self.camera["zoom"], 1.0 / self.camera["zoom"], 1.0)
            
            GL.glTranslatef(-self.camera["x"] + width/2, -self.camera["y"] + height/2, 0)
        
        # SCALE

        if self.window_settings["stretch"] == stretchType.EXPAND:
            GL.glScalef(self.current_window_sizes[0] / self.window_settings["width"], self.current_window_sizes[1] / self.window_settings["height"], 1.0)

        # BLENDING

        GL.glEnable(GL.GL_BLEND)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)

        # TEXTURE

        GL.glEnable(GL.GL_TEXTURE_2D)
        
        # CHECK UPDATE FUNCTION

        if update:
            update()
        
        # DEBUG ON/OFF
        
        if Keyboard.KeyPressed(Key("shift"), self) and Keyboard.KeyJustPressed(Key("f12"), self) and debug:
            if self.debugmenu in (2, 3):
                self.debugmenu = 0
            else:
                self.debugmenu = 2
        elif Keyboard.KeyPressed(Key("control"), self) and Keyboard.KeyJustPressed(Key("f12"), self) and debug:
            if self.debugmenu in (1, 2):
                self.debugmenu = 0
            else:
                self.debugmenu = 3
        elif Keyboard.KeyJustPressed(Key("f12"), self) and debug:
            if self.debugmenu in (1, 3):
                self.debugmenu = 0
            else:
                self.debugmenu = 1
        
        # DRAW ELEMENTS
        
        for element in self.elements:
            if isinstance(element, SimpleButton):
                element._process(self)
                element._draw(self)
            elif isinstance(element, textInput):
                element._process(self)
                element._draw(self)
        
        # DEBUG SHOW
        
        self.upd_fps_timer.timerProcess(self)
        
        if self.debugmenu == 1 and debug:
            padding = 14
            
            memory_info = self.memorymonitor.getMemory()
            mouse_pos = Mouse.getPosition(self)
            
            text_lines = [
                "===OGE DEBUG===",
                f"FPS:{self.getFPS()}",
                f"Window size:{self.current_window_sizes}",
                f"Mouse pos:{int(mouse_pos.x)} {int(mouse_pos.y)}",
                f"Render objects:{len(render_items)}",
                f"RSS:{memory_info['rss']:.2f}MB",
                f"VMS:{memory_info['vms']:.2f}MB",
                f"Memory peak:{memory_info['peak']:.2f}MB",
                f"Threads:{threading.active_count()}",
                f"Vertexes:{len(render_vertexes)}"
            ]
            
            for index, label in enumerate(text_lines):
                self.drawText(label, Vec2(0, index*padding), debug_only=True)
        elif self.debugmenu == 2 and debug:
            self.drawText(f"FPS: {self.fps}", Vec2(0, 0), debug_only=True)
        
        # WINDOW PROCESS
        
        glfw.swap_buffers(self.window)
        glfw.poll_events()

        # GET FPS

        self.frame_count += 1
        current_time = time.time()
        if current_time - self.last_fps_time >= 1.0:
            self.fps = self.frame_count
            self.frame_count = 0
            self.last_fps_time = current_time

    def winProcess(self, update=None, fps: int | None = None):
        try:
            log_system.addInfo(f"Create winprocess, Update:{update.__name__}, FPS:{fps}")
        except:
            log_system.addInfo(f"Create winprocess, Update:{update}, FPS:{fps}")

        last_time = time.time()

        while not glfw.window_should_close(self.window):
            current_time = time.time()
            elapsed = current_time - last_time

            if fps is not None:
                frame_time = 1.0 / fps

                if elapsed >= frame_time:
                    self._render_frame(update)
                    last_time = current_time
                else:
                    time.sleep(max(0, frame_time - elapsed - 0.001))
            else:
                self._render_frame(update)
                last_time = current_time
        
        glfw.terminate()
