from ...Kernel.modules import GL, threading, keyboard, time, glutBitmapCharacter
from ...Kernel.Components.vectors import Vec2
from ...Kernel.Components.graphics  import Color3, Color4
from ...Kernel.Components.control import MouseButton
from ...Kernel.Components.system import System
from ...Kernel.kernel import classWrapper, logWrapper
from ...Kernel.fonts import fonts
from ...Control.mouse import Mouse

def _resetMatrix(self):
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glPushMatrix()
    GL.glLoadIdentity()
    width, height = self.current_window_sizes
    GL.glOrtho(0, width, height, 0, -1, 1)
    
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glPushMatrix()
    GL.glLoadIdentity()

def _recoveryMatrix():
    GL.glMatrixMode(GL.GL_MODELVIEW)
    GL.glPopMatrix()
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glPopMatrix()
    GL.glMatrixMode(GL.GL_MODELVIEW)

def bgframe(position, size, addcolor):
    color1 = addcolor + Color4(0.3, 0.3, 0.3, 1)
    color2 = addcolor + Color4(0.2, 0.2, 0.2, 1)
    GL.glBegin(GL.GL_POLYGON)
    GL.glColor4f(color1.r, color1.g, color1.b, color1.a)
    GL.glVertex2f(position.x, position.y)
    GL.glVertex2f(position.x + size.x, position.y)
    GL.glColor4f(color2.r, color2.g, color2.b, color2.a)
    GL.glVertex2f(position.x + size.x, position.y + size.y)
    GL.glVertex2f(position.x, position.y + size.y)
    GL.glEnd()

@logWrapper
def _drawText(self, text:str, position:Vec2=Vec2(0.0, 0.0), color:Color3=Color3(1.0, 0.0, 0.0), font=fonts["HELVETICA 12"], debug_only=False, donthide=False, screen_space=True):
    
    # DISABLE TEXT
    if not donthide:
        if self.debugmenu in (1, 2) and not debug_only:
            return
    
    # DISABLE SHADERS

    GL.glUseProgram(0)

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
    
    if screen_space:
        _resetMatrix(self)
    
    GL.glDisable(GL.GL_TEXTURE_2D)
    
    GL.glColor3f(color.r, color.g, color.b)
    GL.glRasterPos2f(position.x, position.y + 10)
    
    for char in str(text):
        glutBitmapCharacter(font, ord(char))
    
    GL.glEnable(GL.GL_TEXTURE_2D)
    
    if screen_space:
        _recoveryMatrix()

@logWrapper
def _drawTextBox(self, text:str, position:Vec2=Vec2(0.0, 0.0), color:Color3=Color3(1.0, 0.0, 0.0), charslen:int=0, bgcolor:Color4=Color4(0.0, 0.0, 0.0, 0.0), font=fonts["HELVETICA 12"], debug_only=False, donthide=False, screen_space=False):
    
    # DISABLE TEXT
    
    if not donthide:
        if self.debugmenu in (1, 2) and not debug_only:
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
    
    char_size = Vec2(6, 12)
    
    chunks = [text[i:i+charslen] for i in range(0, len(text), charslen)]
    
    if screen_space:
        _resetMatrix(self)
    
    bgframe(position, Vec2(char_size.x*charslen, char_size.y*len(chunks)), bgcolor)
    
    for index, chunk in enumerate(chunks):
        _drawText(self, chunk, Vec2(position.x, position.y+index*12), color, font, debug_only)
    
    if screen_space:
        _recoveryMatrix()

@classWrapper
class SimpleButton:
    def __init__(self, text=str, position:Vec2=Vec2(0.0, 0.0), size:Vec2=Vec2(0.0, 0.0), fgcolor:Color3|Color4=Color4(0.0, 0.0, 0.0, 0.0), func=None, font=fonts["HELVETICA 12"]):
        
        # COLORS
        
        self.normalColor = Color4(0, 0, 0, 0)
        self.hoverColor = Color4(-0.05, -0.05, -0.05, 0)
        self.pressedColor = Color4(-0.1, -0.1, -0.1, 0)

        # VALUES

        self.text = text
        self.position = position
        self.size = size
        self.fgcolor = fgcolor
        self.func = func
        self.font = font
        
        # DYNAMIC VALUE
        
        self.hovered = False
        self.clicked = False
        self.funcactivated = False
        
        # THREAD
        
        self.thread = None
        self.lock = threading.Lock()

    def _draw(self, window):
        
        GL.glDisable(GL.GL_TEXTURE_2D)
        
        # DRAWING BG
        
        if self.clicked:
            bgframe(self.position, self.size, self.pressedColor)
        elif self.hovered:
            bgframe(self.position, self.size, self.hoverColor)
        else:
            bgframe(self.position, self.size, self.normalColor)

        # DRAW TEXT

        _drawText(window, self.text, self.position, self.fgcolor, self.font, False, True, False)
    
    def _process(self, window):
        mousePos = Mouse.getMouseWorld(window)
        
        # HOVER
        
        if mousePos.x >= self.position.x and mousePos.x <= self.position.x + self.size.x:
            if mousePos.y >= self.position.y and mousePos.y <= self.position.y + self.size.y:
                self.hovered = True
            else:
                self.hovered = False
        else:
            self.hovered = False
        
        # CLICK
        
        if Mouse.MouseKeyPressed(window, MouseButton.LEFT) and self.hovered:
            self.clicked = True
        else:
            self.clicked = False

        # RUN FUNCTION IF CLICKED
        
        if self.clicked and not self.funcactivated:
            self.funcactivated = True
            if self.func:
                with self.lock:
                    self.thread = threading.Thread(target=self.func, daemon=True, name=f"buttonThread-{id(self)}")
                    self.thread.start()
        elif not self.clicked and self.funcactivated:
            self.funcactivated = False

@classWrapper
class textInput:
    def __init__(self, position:Vec2=Vec2(0.0, 0.0), size:Vec2=Vec2(0.0, 0.0), fgcolor:Color3|Color4=Color4(0.0, 0.0, 0.0, 0.0), font=fonts["HELVETICA 12"]):
        
        # COLORS
        
        self.normalColor = Color4(0, 0, 0, 0)
        self.selectedColor = Color4(-0.1, -0.1, -0.1, 0)

        # VALUES

        self.value = ""
        self.position = position
        self.size = size
        self.fgcolor = fgcolor
        self.font = font
        
        # DYNAMIC VALUE
        
        self.selected = False
        self.keypressed = ""
        self.keylasttime = 0
        self.window = None
        
        keyboard.on_press(self._key_pressed)

    def getValue(self):
        return self.value

    def setValue(self, text:str):
        self.value = text

    def _process(self, window):
        mousePos = Mouse.getMouseWorld(window)
        
        # SELECT
        
        if mousePos.x >= self.position.x and mousePos.x <= self.position.x + self.size.x:
            if mousePos.y >= self.position.y and mousePos.y <= self.position.y + self.size.y:
                if Mouse.MouseKeyPressed(window, MouseButton.LEFT):
                    self.selected = True
                    window.selected_keyboard = self
            else:
                if Mouse.MouseKeyPressed(window, MouseButton.LEFT):
                    self.selected = False
                    if window.selected_keyboard == self:
                        window.selected_keyboard = None
        else:
            if Mouse.MouseKeyPressed(window, MouseButton.LEFT):
                self.selected = False
                if window.selected_keyboard == self:
                    window.selected_keyboard = None
        
        if not self.window:
            self.window = window

    def _key_pressed(self, event):
        if not self.selected:
            return
        key = event.name
        if len(key) == 1 and key.isalpha() or key in ["backspace", "enter"] or key in "1234567890":
            if key == self.keypressed:
                if time.time() >= self.keylasttime + 0.0020:
                    self._key_handle(key)
            else:
                self._key_handle(key)
    
    def _key_handle(self, key):
        match key:
            case "backspace": # DEL LAST CHAR
                self.keylasttime = time.time()
                self.keypressed = key
                self.value = self.value[:-1]

            case "enter": # DESELECT
                self.selected = False
                self.window.selected_keyboard = None
            
            case _: # WRITE CHAR
                self.value += key
                self.keylasttime = time.time()
                self.keypressed = key

    def _draw(self, window):
        
        # DRAWING BG
        
        GL.glDisable(GL.GL_TEXTURE_2D)
        
        if self.selected:
            bgframe(self.position, self.size, self.selectedColor)
        else:
            bgframe(self.position, self.size, self.normalColor)

        # DRAW TEXT

        _drawText(window, self.value, self.position, self.fgcolor, self.font, False, True)
