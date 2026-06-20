# OpenGameEngine
Game engine maded on OpenGL, Python 3.12

## Tutorial
### Run
**IF YOU ARE USING LINUX AND USING KeyPressed - RUN AS ROOT!!!**

IF YOU ARE USING WINDOWS, JUST RUN THE PYTHON FILE AS USUAL.

**MACOS NOT SUPPORTED!!!**

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
    
    # Get mouse position
    mouse_pos = window.getMousePosition()
    
    # Get current window sizes
    cur_winsize = window.current_window_sizes

# Run window mainloop, 1 arg - update function, 2 arg - window fps
window.winProcess(update, 60)
```

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
+ getCenter - getting the center of the primitive.

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

### Control
```python
KeyPressed(Key("space")) # Return bool value, if key is pressed - True else False. arg1 - Key
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
    if KeyPressed(Key("w")):
        player.position.y -= 8
    elif KeyPressed(Key("s")):
        player.position.y += 8
    
    if KeyPressed(Key("a")):
        player.position.x -= 8
    elif KeyPressed(Key("d")):
        player.position.x += 8
    
    player.calculateSize()
    player.drawRectangle(drawMode.FILL)

window.winProcess(update, 60)
```
