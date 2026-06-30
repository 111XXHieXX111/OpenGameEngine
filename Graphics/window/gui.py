from ...Core.modules import GL, threading, keyboard, time, glutBitmapCharacter, GLUT_BITMAP_HELVETICA_12  # type: ignore
from ...Core.base import Vec2, System, Color3, Color4, drawMode, MouseButton
from ...Core.glob import classWrapper, logWrapper
from ...Control.mouse import Mouse
from ..objects.rectangle import Rectangle

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
def _drawText(self, text:str, position:Vec2=Vec2(0.0, 0.0), color:Color3=Color3(1.0, 0.0, 0.0), debug_only=False, donthide=False):
    
    # DISABLE TEXT
    
    if not donthide:
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

@logWrapper
def _drawTextBox(self, text:str, position:Vec2=Vec2(0.0, 0.0), color:Color3=Color3(1.0, 0.0, 0.0), charslen:int=0, bgcolor:Color4=Color4(0.0, 0.0, 0.0, 0.0), debug_only=False, donthide=False):
    
    # DISABLE TEXT
    
    if not donthide:
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
    
    char_size = Vec2(6, 12)
    
    chunks = [text[i:i+charslen] for i in range(0, len(text), charslen)]
    
    rect = Rectangle(self)
    rect.setPosition(position)
    rect.setSize(Vec2(char_size.x*charslen, char_size.y*len(chunks)))
    rect.setColor(bgcolor)
    rect.drawRectangle(drawMode.FILL)
    
    for index, chunk in enumerate(chunks):
        _drawText(self, chunk, Vec2(position.x, position.y+index*12), color, debug_only)

@classWrapper
class SimpleButton:
    def __init__(self, text=str, position:Vec2=Vec2(0.0, 0.0), size:Vec2=Vec2(0.0, 0.0), fgcolor:Color3|Color4=Color4(0.0, 0.0, 0.0, 0.0), func=None):
        
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
        
        # DYNAMIC VALUE
        
        self.hovered = False
        self.clicked = False
        self.funcactivated = False
        
        # THREAD
        
        self.thread = None
        self.lock = threading.Lock()

    def _draw(self, window):
        
        # DRAWING BG
        
        if self.clicked:
            bgframe(self.position, self.size, self.pressedColor)
        elif self.hovered:
            bgframe(self.position, self.size, self.hoverColor)
        else:
            bgframe(self.position, self.size, self.normalColor)

        # DRAW TEXT

        _drawText(window, self.text, self.position, self.fgcolor, False, True)
    
    def _process(self, window):
        mousePos = Mouse.getPosition(window)
        
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
    def __init__(self, position:Vec2=Vec2(0.0, 0.0), size:Vec2=Vec2(0.0, 0.0), fgcolor:Color3|Color4=Color4(0.0, 0.0, 0.0, 0.0)):
        
        # COLORS
        
        self.normalColor = Color4(0, 0, 0, 0)
        self.selectedColor = Color4(-0.1, -0.1, -0.1, 0)

        # VALUES

        self.value = ""
        self.position = position
        self.size = size
        self.fgcolor = fgcolor
        
        # DYNAMIC VALUE
        
        self.selected = False
        self.keypressed = ""
        self.keylasttime = 0
        self.window = None

    def getValue(self):
        return self.value

    def setValue(self, text:str):
        self.value = text

    def _process(self, window):
        mousePos = Mouse.getPosition(window)
        
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
        
        if self.selected:
            keyboard.on_press(self._key_pressed)
    
    def _key_pressed(self, event):
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
        
        if self.selected:
            bgframe(self.position, self.size, self.selectedColor)
        else:
            bgframe(self.position, self.size, self.normalColor)

        # DRAW TEXT

        _drawText(window, self.value, self.position, self.fgcolor, False, True)
