from ...Core.modules import glfw, GL, time, glutInit, glutBitmapCharacter, GLUT_BITMAP_HELVETICA_12 # type: ignore
from ...Core.glob import log_system, debug, render_items
from ...Core.base import System, Color3, Color4, stretchType, Vec2, Key
from ...Utils.memory import MemoryMonitor
from ...Control.keyboard import Keyboard
from ...Control.mouse import Mouse

class Window:
    def __init__(self):

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

        self.frame_count = 0
        self.fps = 0
        self.last_fps_time = time.time()
        
        self.iconified = 0
        self.iconifiedwork = True
        
        self.debugmenu = False

        # CURRENT SIZES

        log_system.addInfo("Create current win sizes")

        self.current_window_sizes = [640, 480]

    def _iconify_callback(self, window, iconified):
        self.iconified = iconified

    def initWindow(self):
        
        log_system.addInfo("Init window")
        
        # CREATE WINDOW

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
        
        self.momorymonitor = MemoryMonitor()

        # MOVE WINDOW TO THE CURRENT CONTEXT

        log_system.addInfo("Move window to the current context")
        
        glfw.make_context_current(self.window)

        # VSYNC

        glfw.swap_interval(0)

        # GET CURRENT WINDOW SIZES

        log_system.addInfo("Get current win sizes")

        self.current_window_sizes = glfw.get_framebuffer_size(self.window)
        
        # CONNECT CALLBACK(S)
        
        glfw.set_window_iconify_callback(self.window, self._iconify_callback)

    def setStretch(self, stretch:stretchType):
        log_system.addInfo("Setting stretch")
    
        # APPLY STRETCH
        
        self.window_settings["stretch"] = stretch
    
    def getFPS(self):
        return self.fps

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

    def drawText(self, text:str, position:Vec2=Vec2(0.0, 0.0), color:Color3=Color3(1.0, 0.0, 0.0), *, debug_only=False):
        
        # DISABLE TEXT
        
        if self.debugmenu and not debug_only:
            return
        
        # CHECK TYPES
        
        if not isinstance(text, str):
            return
        
        if not isinstance(position, Vec2):
            if isinstance(position, list) or isinstance(position, tuple):
                position = System.cltv2(position)
        
        if not isinstance(color, Color3):
            if isinstance(color, Color4):
                color = Color3(color.r, color.b, color.g) 
            elif isinstance(color, list) or isinstance(color, tuple):
                color = Color3(color[0], color[1], color[2])
            else:
                return
        
        # SET COLOR AND POSITION
        
        GL.glColor3f(color.r, color.g, color.b)
        GL.glRasterPos2f(position.x, position.y+10)
        
        # DRAW CHARS
        
        for char in str(text):
            glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ord(char))
    
    def _render_frame(self, update=None):
        
        # GET CURRENT WINDOW SIZES

        self.current_window_sizes = list(glfw.get_framebuffer_size(self.window))
        
        # SKIP RENDER
        
        if self.current_window_sizes[0] <= 0 or self.current_window_sizes[1] <= 0:
            glfw.poll_events()
            
            return
        
        # CLEAR RENDER ITEMS
        
        render_items.clear()

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

        # MODELVIEW MATRIX

        GL.glMatrixMode(GL.GL_MODELVIEW)
        GL.glLoadIdentity()

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
        
        if Keyboard.KeyJustPressed(Key("f12"), self) and debug:
            self.debugmenu = not self.debugmenu
        
        # DEBUG SHOW
        
        if self.debugmenu and debug:
            padding = 14
            
            memory_info = self.momorymonitor.getMemory()
            mouse_pos = Mouse.getPosition(self)
            
            text_lines = [
                "===OGE DEBUG===",
                f"FPS:{self.getFPS()}",
                f"Window size:{self.current_window_sizes}",
                f"Mouse pos:{int(mouse_pos.x)} {int(mouse_pos.y)}",
                f"Render objects:{len(render_items)}",
                f"RSS:{memory_info['rss']:.2f}MB",
                f"VMS:{memory_info['vms']:.2f}MB",
                f"Memory peak:{memory_info['peak']:.2f}MB"
            ]
            for index, label in enumerate(text_lines):
                self.drawText(label, Vec2(0, index*padding), debug_only=True)

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
            log_system.addInfo(f"Create winprocess, Update:{update.__name__}, FPS:{fps}") # type: ignore
        except:
            log_system.addInfo(f"Create winprocess, Update:{update}, FPS:{fps}")

        # CHECK FPS

        if fps is not None:
            frame_time = 1.0 / fps
            last_time = time.time()
        
        # RENDER LOOP

        while not glfw.window_should_close(self.window):
            if fps is not None:
                current_time = time.time()
                elapsed = current_time - last_time

                if elapsed >= frame_time:
                    self._render_frame(update)
                    last_time = current_time
                else:
                    time.sleep(frame_time - elapsed)
            else:
                self._render_frame(update)

        glfw.terminate()
