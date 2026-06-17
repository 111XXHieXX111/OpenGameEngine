# OpenGameEngine
Game engine maded on OpenGL, Python 3.12

## Tutorial
### Main
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
