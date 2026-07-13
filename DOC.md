# Tutorial
## Run
**IF YOU ARE USING LINUX - RUN AS ROOT!!!**

IF YOU ARE USING WINDOWS, JUST RUN THE PYTHON FILE AS USUAL.

**MACOS NOT SUPPORTED!!!**

## Import
```python
# Import game lib
from OpenGameEngine import *
```

## Compontents

### Vectors

```python
vec1 = Vec1(0.0, 0.0)
vec2 = Vec2(0.0, 0.0)
```

### Graphics

```python

# COLORS

color3 = Color3(0.0, 0.0, 0.0)
color4 = Color4(0.0, 0.0, 0.0, 0.0)
color256 = c256(0)

# OTHER

drawmode = drawMode.FILL        # drawMode has: POINTS, LOOP, FORM, FILL, RECT
textype = textureType.LINEAR    # textureType has: LINEAR, NEAREST
stype = stretchType.KEEP_ASPECT # stretchType has: EXPAND, RELATIVELY, KEEP_ASPECT
bdrawing = batchDrawing.STATIC # batchDrawing has: STATIC, DYNAMIC
```

### Control

```python
key = Key("space")
```

## Window
```python
# Creating window
window = Window(0)

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
    window.drawText(str(fps), Vec2(0, 0), Color3(1, 0, 0)) # arg1 - text, arg2 - position, arg3 - color

    # Get current window sizes
    cur_winsize = window.current_window_sizes

# Run window mainloop, 1 arg - update function, 2 arg - window fps
window.winProcess(update, 60)
```

To open the unlock menu, press **F12**

Window has methods addElement/removeElement
+ addElement - add element in window, arg1 - SimpleButton | textInput
+ removeElement - remove element in window, arg1 - SimpleButton | textInput

```python
btn = SimpleButton("Button", Vec2(0.0, 0.0), Vec2(0.0, 0.0), Color3(0.0, 0.0, 0.0), None) # arg1 - text, arg2 - position, arg3 - size, arg4 - text color (fg), arg5 - function (optional), arg6 - fonts (optional)
window.addElement(btn)                                                                    # Rendering is automatic
```

```python
inp = textInput(Vec2(0.0, 0.0), Vec2(0.0, 0.0), Color3(0.0, 0.0, 0.0)) # arg1 - position, arg2 - size, arg3 - color, arg4 - fonts (optional)
inp.getValue()                                                         # Return current text
inp.setValue("Text")                                                   # Set text, arg1 - str
window.addElement(inp)                                                 # Rendering is automatic
```

Window has method drawText
+ drawText - drawing any text in window, arg1 - text, arg2 - position, arg3 - text color (fg), arg4 - fonts (optional), arg5 - bool (if True - Stick to the window, else - Stay in place)

```python
def update(): # Function in winProcess
    window.drawText("Hello, World!", Vec2(0.0, 0.0), Color3(0.0, 0.0, 0.0))
```

window has methods enableEventsByIconify/disableEventsByIconify
+ window.enableEventsByIconify - Enable events when window is minimized
+ window.disableEventsByIconify - Disable events when window is minimized

**Cyrillic is not supported in the drawText function!**

**Window** takes an **int** as the first argument; if 0, it uses the new rendering method (**VBO**, **VAO**); if 1, it uses the old **vertex**-based method.

## Graphics

### Load texture
```python
loadTexture("texturepath/texture.png", textureType.LINEAR) # Load texture, arg1 - path, arg2 - textureType
```

### Primitives
```python
rectangle = Graphics.Rectangle() # arg1 - window (optional) (for optimization)
triangle = Graphics.Triangle() # arg1 - window (optional) (for optimization)
circle = Graphics.Circle() # arg1 - int, number of segments (default 8), arg2 - window (optional) (for optimization)

vertex = Graphics.Vertex()
polygon = Graphics.Polygon([]) # Arg is vertexes list
```

If you write **window** as the 1st argument, then if a **primitive** goes outside the visible area (does not work with the **camera**), it will not be rendered.

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

There is also a **checkCollision** function, it checks whether the first primitive touches the second one. 
**Note:** This function uses AABB (Axis-Aligned Bounding Box). It creates an axis-aligned rectangle around each shape, so for rotated objects the collision area will be larger than the actual shape. For non-rotated objects it works perfectly.

```python
if checkCollision(rect1.vertexes, rect2.vertexes):
    print("Colliding")
```

Primitives such as **Rectangle**, **Triangle**, **Circle** need to call the calculateSize function in order to calculate the size, and it is called **BEFORE draw**

Draw modes:
+ POINTS
+ LOOP
+ FORM
+ FILL
+ RECT

### Batch

```python
render = batchRender(batchDrawing.STATIC) # batchDrawing (STATIC - for static primitives, add it once. DYNAMIC - for dynamic primitives and are added to update.)
render.addPrimitive(rect)                 # Add primitive (Only Rectangle, Triangle. Textures not supported!!! Don't use draw for batch)
render.setDrawMode(drawMode.FILL)        # Set drawMode for primitives
render.renderPrimitives()                 # Draw primitives, place in update
```

### SimpleParticles

```python
particles = Graphics.simpleParticles()        # arg1 - window (optional) (for optimization)
particles.setPosition(Vec2(0.0, 0.0))         # Set particles position, arg1 - Vec2
particles.setColor(Color3(0.0, 0.0, 0.0))     # Set particles color, arg1 - Color3 | Color4
particles.setSize(Vec2(0.0, 0.0))             # Set particles size, arg1 - Vec2
particles.setGravity(Vec1(0.0))               # Set particles gravity, arg1 - Vec1
particles.setSpawnRadius(Vec2(0.0, 0.0))      # Set particles spawn radius (box shape), arg1 - Vec2
particles.setLifetime(0.0)                    # Set particles life time, arg1 - int | float (if timer type == Timer: float | int, else: int)
particles.setTexture(None)                    # Set particles texture, arg1 - loaded texture
particles.setDirectionX(Vec1(0.0))            # Set particles direction in axis X (offset), arg1 - Vec1 (-1 left, 1 right, you can have any values)
particles.setRandomRotation(Vec1(0.0))        # Set particles random rotation, arg1 - Vec1 (max rotation)
particles.setRandomSize(Vec2(0.0, 0.0), None) # Set particles random size, arg1 - Vec2 (maximum deviation from the base size in X and Y), arg2 - Bool (Answers whether random sizes will be the same.)
particles.setRandomDirectionX(Vec2(0.0, 0.0)) # Set particles random direction, arg1 - Vec2 (value1 - minimum posX, value2 - maximum)
particles.setMaxParticles(0)                  # Set max drawing particles, arg1 - int
particles.setRandomColor(False)               # Set random color, arg1 - bool (if True - enabled else disabled random)
particles.setTimerType(Timer)                 # Set timer type, arg1 - Timer | frameTimer
particles.drawParticles()                     # Draw particles, arg1 - dt (Optional), arg2 - Window (if timerType == Timer: required, else: dont't)
```

### Sprite

```python
sprite = Sprite(None, None) # arg1 - Window, arg2 - Update function
sprite.setPosition(Vec2(0.0, 0.0)) # arg1 - Vec2
sprite.setSize(Vec2(0.0, 0.0)) # arg2 - Vec2
sprite.setColor(Color4(0.0, 0.0, 0.0, 0.0)) # arg1 - Color3 | Color4
sprite.customData.update({"Data":None}) # add custom data
sprite.spriteProcess() # Drawing sprite
```

## Control
```python
# Keyboard
Keyboard.KeyPressed(Key("space"), Window)        # Return bool value, if key is pressed - True else False. arg1 - Key, arg2 - Window
Keyboard.KeyJustPressed(Key("space"), Window)    # Return bool value, if key is just pressed - True else False, arg1 - Key, arg2 - Window

# Mouse:
Mouse.getPosition(Window)                        # Return position in Vec2, arg1 - Window
Mouse.MouseKeyPressed(Window, MouseButton.LEFT)  # Return bool value, if key is pressed - True else False, arg1 - Window, arg2 - MouseButton
Mouse.MouseKeyReleased(Window, MouseButton.LEFT) # Return bool value, if key is released - True else False, arg1 - Window, arg2 - MouseButton
Mouse.setVisibility(Window, True)                # Sets the mouse visibility, arg1 - Window, arg2 - Bool If set to True, it is visible, if set to False, it is invisible but not captured.
```

## Other

### frameTimer

```python
def test_func():
    print("Hello, World!")

timer = frameTimer(60, test_func) # arg1 - target frame, arg2 - func

def update():
    timer.timerProcess()
```

The function is triggered when the current frame is the same in count as the number of the target. When the goal is reached, the timer is reset and so on in a circle.

### Timer

```python
def test_func():
    print("Hello, World!")

timer = Timer(2, test_func)    # arg1 - target sec, arg2 - func

def update():
    timer.timerProcess(window) # arg1 - window
```

### dataSave

```python

key = genKey()                     # Generate random key

data = {                           # Your data
    "a":2
}

saveData("save.dat", data, key)    # Save data to file, arg1 - path, arg2 - data, arg3 - key

loaded = loadData("save.dat", key) # Load data, arg1 - path, arg2 - key

print(loaded)

```

### sceneManager

**Scene manager:**

```python
scenes = sceneManager()          # Create scene manager
scenes.addScene("Scene 1", sceneclass) # Add your scene, arg1 - name, arg2 - scene class
scenes.selectScene("Scene 1")    # Select scene, arg1 - name
scenes.removeScene("Scene 1")    # Remove your scene, arg1 - name
scenes.sceneProcess()            # Place in update
```

**Scene class:**

```python
class scene:
    def sceneInit(self):
        pass # Init your scene
    
    def sceneProcess(self):
        pass # Update your scene
```

### logSystem

```python
log_system.addInfo("Info message")                   # Add info log, arg1 - str
log_system.addWarn("Warning message")                # Add warning log, arg1 - str
log_system.addError("Error message")                 # Add error log, arg1 - str
log_system.addCritical("Critical message")           # Add critical log, arg1 - str
log_system.consoleStream(True)                       # Enable/disable console output, arg1 - bool
log_system.getLog()                                  # Print all logs
log_system.saveLog()                                 # Save logs to timestamp_log.txt
```

### checkInDebbuger

```python
checkInDebbuger() # Return True if running under debugger, False otherwise
```

### icons

```python
icons["Icon"]    # png icon
icons["HRIcon"]  # high resoultion png icon
icons["IcoIcon"] # ico icon
```

### fonts

```python
fonts["HELVETICA 10"]
fonts["HELVETICA 12"]
fonts["HELVETICA 18"]
fonts["ROMAN 10"]
fonts["ROMAN 24"]
```

## Sound

### loadSound

```python
sound = loadSound("sound.wav", "float32") # Load sound, arg1 - audio file, arg2 - type (optional)
sound.play(None)                          # Play loaded sound, arg1 - loop (bool) (optional)
sound.stop()                              # Stop playing sound
sound.isPlaying()                         # Return is playing sound
sound.getVolume()                         # Return sound volume
sound.setVolume(0.0)                      # Set sound volume
```

### soundManager

```python
manager = soundManager()
manager.addSound("sound", loadSound("sound.wav")) # Add sound, arg1 - name, arg2 - loaded sound
manager.playSound("sound")                        # Play sound, arg1 - name
manager.stopSound("sound")                        # Stop sound, arg1 - name
manager.isPlayingSound("sound")                   # Return is playing sound, arg1 - name
manager.setSoundVolume("sound", 0.0)              # Set sound volume, arg1 - name, arg2 - volume
manager.getSoundVolume("sound")                   # Return sound volume, arg1 - name
manager.setGeneralVolume(0.0)                     # Set volume for alls sounds, arg1 - volume
manager.stopSounds()                              # Stop all sounds
manager.getSound("sound")                         # Return sound, arg1 - name
manager.removeSound("sound")                      # Remove sound, arg1 - name
```
