# OpenGameEngine
Game engine maded on OpenGL, Python 3.12

## Tutorial
### Run
**IF YOU ARE USING LINUX - RUN AS ROOT!!!**

IF YOU ARE USING WINDOWS, JUST RUN THE PYTHON FILE AS USUAL.

**MACOS NOT SUPPORTED!!!**

### Install modules
```bash
pip install PyOpenGL PyOpenGL_accelerate glfw keyboard Pillow psutil
```

### Import
```python
# Import game lib
from OpenGameEngine import *
```

### Base Classes & Functions
```python
# Vectors, vectors has method "getVectors"

vec1 = Vec1(0, 0)
vec2 = Vec2(0, 0)

# Colors

color3 = Color3(0, 0, 0)    # RGB
color4 = Color4(0, 0, 0, 0) # RGBA
color256 = c256(128)        # Convert 0-255 to 0-1

# Binds

key = Key("space") # Key has method "getKey"

# Drawing

drawmode = drawMode.FILL # drawMode has: POINTS, LOOP, FORM, FILL, RECT

# Textures

textype = textureType.LINEAR # textureType has: LINEAR, NEAREST

# Window stretching

stype = stretchType.KEEP_ASPECT # stretchType has: EXPAND, RELATIVELY, KEEP_ASPECT

```

### Window
```python
# Creating window
window = Window()

# Init window
window.initWindow()

# Set window title "Game"
window.setTitle("Game")

# Set window resolution 640x480
window.setSize(640, 480)

# Set window back color
window.setBG(Color3(0, 0.5, 1))

# Update function
def update():
    # Get window fps
    fps = window.getFPS()
    
    # Show fps
    window.drawText(str(fps), Vec2(0, 0), Color3(1, 0, 0)) # 1 arg - text, 2 arg - position, 3 arg - color

    # Get current window sizes
    cur_winsize = window.current_window_sizes

# Run window mainloop, 1 arg - update function, 2 arg - window fps
window.winProcess(update, 60)
```

To open the unlock menu, press F12

### Graphics

#### Load texture
```python
loadTexture("texturepath/texture.png", textureType.LINEAR) # Load texture, arg1 - path, arg2 - textureType
```

#### Primitives
```python
rectangle = Graphics.Rectangle()
triangle = Graphics.Triangle()
circle = Graphics.Circle()

vertex = Graphics.Vertex()
polygon = Graphics.Polygon([]) # Arg is vertexes list
```
**ALL primitives** have functions such as:
+ setWidthLines - setting the line width;
+ setSize - setting the size of the primitive;
+ setPosition - setting the position of the primitive;
+ setRotation - setting the rotation of the primitive;
+ setColor - setting the color of the primitive;
+ setUV - setting the UV mapping position;
+ setTexture - setting the texture;
+ getCenter - getting the center of the primitive;
+ setPointSize - setting the vertex size.

There is one more very important function: **draw**, only it is not in the usual form, the formula is as follows: **draw** + the name of the primitive with a capital letter. Examples:
```python
rectangle.drawRectangle(drawMode.FILL)       # arg1 - drawMode
triangle.drawTriangle(drawMode.FILL)         # arg1 - drawMode
circle.drawCircle(drawMode.FILL)             # arg1 - drawMode
vertex.drawVertex(True, True, drawMode.FILL) # arg1 - begin, arg2 - end, arg3 - drawMode
polygon.drawPolygon(drawMode.FILL)           # arg1 - drawMode
```

**Important! draw** must be placed in the function specified by **Window** in **winProcess**

There is also a **checkcollision** function, it checks whether the first primitive touches the second one. Primitives such as **Rectangle**, **Triangle**, **Circle** need to call the calculateSize function in order to calculate the size, and it is called **BEFORE draw**

Draw modes:
+ POINTS
+ LOOP
+ FORM
+ FILL
+ RECT

### Control
```python
# Keyboard
Keyboard.KeyPressed(Key("space"), Window)         # Return bool value, if key is pressed - True else False. arg1 - Key, arg2 - Window (optional)
Keyboard.KeyJustPressed(Key("space"), Window)     # Return bool value, if key is just pressed - True else False, arg1 - Key, arg2 - Window (optional)

# Mouse:
Mouse.getPosition()                              # Return position in Vec2
Mouse.MouseKeyPressed(Window, MouseButton.LEFT)  # Return bool value, if key is pressed - True else False, arg1 - Window, arg2 - MouseButton
Mouse.MouseKeyReleased(Window, MouseButton.LEFT) # Return bool value, if key is released - True else False, arg1 - Window, arg2 - MouseButton
Mouse.setVisibility(Window, True)                # Sets the mouse visibility, arg1 - Window, arg2 - Bool If set to True, it is visible, if set to False, it is invisible but not captured.
```

### Game example
```python
from OpenGameEngine import *

window = Window()
window.initWindow()
window.setTitle("Example game")
window.setSize(640, 480)
window.setStretch(stretchType.KEEP_ASPECT)
window.setBG(Color3(0, 0.5, 0))

player = Graphics.Rectangle()
player.setPosition(Vec2(20, 20))
player.setSize(Vec2(60, 60))
player.setColor(Color3(0, 0, 0))

def update():
    if KeyPressed(Key("w"), window):
        player.position.y -= 8
    elif KeyPressed(Key("s"), window):
        player.position.y += 8
    
    if KeyPressed(Key("a"), window):
        player.position.x -= 8
    elif KeyPressed(Key("d"), window):
        player.position.x += 8
    
    player.calculateSize()
    player.drawRectangle(drawMode.FILL)

window.winProcess(update, 60)
```

```python
from OpenGameEngine import *

window = Window()
window.initWindow()
window.setTitle("Collision game")
window.setSize(640, 480)
window.setStretch(stretchType.EXPAND)
window.setBG(Color3(0, 0, 0))

rect = Rectangle()
rect.setPosition(Vec2(60, 60))
rect.setSize(Vec2(20, 20))
rect.setColor(Color3(1, 1, 1))

collide = Rectangle()
collide.setPosition(Vec2(120, 60))
collide.setSize(Vec2(20, 20))
collide.setColor(Color3(1, 0, 0))

inv = False

def update():
    global inv
    
    rect.drawRectangle(drawMode.FILL)
    collide.drawRectangle(drawMode.LOOP)
    
    colliding = checkCollision(rect.vertexes, collide.vertexes)
    
    window.drawText(str(f"Colliding:{colliding}"), Vec2(0, 0), Color3(1, 0, 0))

    if inv:
        rect.position.x -= 2
    else:
        rect.position.x += 2
    
    if rect.position.x >= 180:
        inv = True
    elif rect.position.x <= 60:
        inv = False
    
    rect.calculateSize()

window.winProcess(update, 60)
```

```python
from OpenGameEngine import *

window = Window()
window.initWindow()
window.setBG(Color3(0, 0.5, 0))
window.setTitle("Dragging")

rect = Rectangle()
rect.setPosition(Vec2(20, 20))
rect.setSize(Vec2(40, 40))
rect.setColor(Color3(0, 0, 0))

mouserect = Rectangle()
mouserect.setSize(Vec2(10, 10))

def update():
    mousePos = Mouse.getPosition(window)
    
    McenterX = mousePos.x - mouserect.size.x / 2
    McenterY = mousePos.y - mouserect.size.y / 2
    
    mouserect.setPosition(Vec2(McenterX, McenterY))
    mouserect.calculateSize()
    
    if Mouse.MouseKeyPressed(window, MouseButton.LEFT):
        if checkCollision(mouserect.vertexes, rect.vertexes):
            RcenterX = mouserect.position.x - rect.size.x / 2
            RcenterY = mouserect.position.y - rect.size.y / 2
            
            rect.setPosition(Vec2(RcenterX, RcenterY))
            rect.calculateSize()
    
    rect.drawRectangle(drawMode.FILL)

window.winProcess(update)
```
