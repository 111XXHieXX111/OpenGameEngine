from ...Core.modules import GL, threading, glutBitmapCharacter, GLUT_BITMAP_HELVETICA_12  # type: ignore
from ...Core.base import Vec2, System, Color3, Color4, drawMode, MouseButton
from ...Control.mouse import Mouse
from ..objects.rectangle import Rectangle

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

class SimpleButton:
    def __init__(self, text=str, position:Vec2=Vec2(0.0, 0.0), size:Vec2=Vec2(0.0, 0.0), fgcolor:Color3|Color4=Color4(0.0, 0.0, 0.0, 0.0), func=None):
        
        # COLORS
        
        self.normalColor = Color3(0.4, 0.4, 0.4)
        self.hoverColor = Color3(0.3, 0.3, 0.3)
        self.pressedColor = Color3(0.2, 0.2, 0.2)
        
        # RECT
        
        self.rect = Rectangle()

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
        
        # DRAW RECT
        
        self.rect.setPosition(self.position)
        self.rect.setSize(self.size)
        self.rect.calculateSize()
        self.rect.drawRectangle(drawMode.FILL)
        
        # SET RECT COLOR
        
        if self.clicked:
            self.rect.setColor(self.pressedColor)
        elif self.hovered:
            self.rect.setColor(self.hoverColor)
        else:
            self.rect.setColor(self.normalColor)

        # DRAW TEXT

        _drawText(window, self.text, self.position, self.fgcolor, False, True)
    
    def _process(self, window):
        mousePos = Mouse.getPosition(window)
        
        # HOVER
        
        if mousePos.x >= self.rect.position.x and mousePos.x <= self.rect.position.x + self.rect.size.x:
            if mousePos.y >= self.rect.position.y and mousePos.y <= self.rect.position.y + self.rect.size.y:
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
