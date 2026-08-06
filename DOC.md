# Tutorial
## Run
Supported:
+ Windows (7+)
+ Linux (Not mobile)
+ Unix-like
+ MacOS (Maybe)
+ ReactOS (Not stable (Problems are not on the side of the engine))

Not supported:
+ Android
+ iOS
+ Haiku
+ KolibriOS

## Import
```python
# Import game lib
from OpenGameEngine import *
```

## Components

### Vectors

```python
vec1 = Vec1(0.0)
vec2 = Vec2(0.0, 0.0)
```

Operations with Vectors:
+ Vector + Vector
+ Vector - Vector
+ Vector * Vector | float | int
+ Vector / Vector | float | int

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
bdrawing = batchDrawing.STATIC  # batchDrawing has: STATIC, DYNAMIC
tmrender = tileMapRender.RECTS  # tileMapRender has: RECTS, BATCH
tween = tweenType.LINEAR        # tweenType has: LINEAR, EASE_IN_OUT
```

### Control

```python
key = Key("space")
Keys # <- KEY

MouseButton. # <- BUTTON

kEvent. # <- EVENT
mEvent. # <- EVENT
```

MouseButton has values such as:
+ LEFT
+ RIGHT
+ MIDDLE
+ BUTTON_4
+ BUTTON_5
+ BUTTON_6
+ BUTTON_7
+ BUTTON_8

kEvent has values such as:
+ Pres - Keyboard.KeyPressed
+ justP - Keyboard.KeyJustPressed

mEvent has values such as:
+ Pres - Mouse.MouseKeyPressed
+ Rel - Mouse.MouseKeyReleased

Keys has values such as:
+ W - Key("w")
+ S - Key("s")
+ A - Key("a")
+ D - Key("d")

+ UP - Key("up")
+ DOWN - Key("down")
+ LEFT - Key("left")
+ RIGHT - Key("right")

+ SPACE - Key("space")
+ ESC - Key("escape")
+ TAB - Key("tab")

+ SHIFT - Key("shift")
+ CONTROL - Key("control")
+ ALT - Key("alt")

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

# Quit window fullscreen (default not in fullscreen)

window.setFullscreen(False)

# Disable fullscreen switch (default True)

window.setFullscreenSwitching(False)

# Update function
def update():
    # Get window fps
    fps = window.getFPS()
    dt = window.getDelta()
    
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
+ drawText - drawing any text in window, arg1 - text, arg2 - position, arg3 - text color (fg), arg4 - fonts (optional)

```python
def update(): # Function in winProcess
    window.drawText("Hello, World!", Vec2(0.0, 0.0), Color3(0.0, 0.0, 0.0))
```

window has methods enableEventsByIconify/disableEventsByIconify
+ window.enableEventsByIconify - Enable events when window is minimized
+ window.disableEventsByIconify - Disable events when window is minimized

**Cyrillic is not supported in the drawText function!**

**Window** takes an **int** as the first argument; if 0, it uses the new rendering method (**VBO**, **VAO**); if 1, it uses the old **vertex**-based method.

```python
window.setCameraPosition(Vec2(0.0, 0.0)) # arg1 - Vec2
window.moveCamera(Vec2(0.0, 0.0))        # arg1 - Vec2
window.setCameraZoom(0.0)                # arg1 - float
window.getCameraPosition()               # Return Vec2
window.setCameraEnabled(False)           # arg1 - bool (Default not enabled)
```

## Graphics

### Load texture
```python
loadTexture("texturepath/texture.png", textureType.LINEAR) # Load texture, arg1 - path, arg2 - textureType
```

### Load shader
```python
loadShader("shaderpath/shader.oshader") # Load shader, arg1 - path, arg2 - uniforms list, function returning Shader (class)
```

Shader values:
+ frag
+ vert
+ program
+ uniforms

### Colors

```python
Colors. # <-COLOR
```

Colors:
+ RED         (1.0, 0.0, 0.0, 1.0)
+ GREEN       (0.0, 1.0, 0.0, 1.0)
+ BLUE        (0.0, 0.0, 1.0, 1.0)
+ WHITE       (1.0, 1.0, 1.0, 1.0)
+ BLACK       (0.0, 0.0, 0.0, 1.0)
+ TRANSPARENT (0.0, 0.0, 0.0, 0.0)
+ YELLOW      (1.0, 1.0, 0.0, 1.0)
+ CYAN        (0.0, 1.0, 1.0, 1.0)
+ PURPLE      (1.0, 0.0, 1.0, 1.0)

```python
random_color3 = randomColor3()
random_color4 = randomColor4() # arg1 - random alpha (bool) (optional) (default:False)
```

### Primitives
```python
rectangle = Graphics.Rectangle(window) # arg1 - window (for optimization) (for new render)
triangle = Graphics.Triangle(window) # arg1 - window (for optimization) (for new render)
circle = Graphics.Circle(window) # arg1 - int, number of segments (default 8), arg2 - window (for optimization) (for new render)

vertex = Graphics.Vertex()
polygon = Graphics.Polygon([]) # arg1 - vertexes list (Vec2s), arg2 - window (NewRender)
polygon = Graphics.PolygonLegacy([]) # Arg is vertexes list (Vec2s) (OldRender)
```

If you write **window** as the 1st argument, then if a **primitive** goes outside the visible area (does not work with the **camera**), it will not be rendered.

Primitives (Rectangle, Triangle, Circle) have functions such as:
+ setWidthLines - setting the line width; (Vec1)
+ setSize - setting the size of the primitive; (Vec2)
+ setPosition - setting the position of the primitive; (Vec2)
+ setRotation - setting the rotation of the primitive; (Vec1)
+ setColor - setting the color of the primitive; (Color3 | Color4)
+ setUV - setting the UV mapping position; (List Vec2s)
+ setTexture - setting the texture; (Texture)
+ getCenter - getting the center of the primitive;
+ setPointSize - setting the vertex size; (Vec1)
+ setShader - settings the shader of the primitive; (Shader)
+ addModule - add module to primitive;
+ isHovered - check if mouse hovered on primitive (You can use: isHovered or isHovered() );
+ isPressed - check if mouse button pressed on primitive; (MouseButton)
And have values:
+ position; (Vec2)
+ size; (Vec2)
+ rotation; (Vec1)
+ color; (Color4, **NOT** Color3)

There is one more very important function: **draw**, only it is not in the usual form, the formula is as follows: **draw** + the name of the primitive with a capital letter. Examples:
```python
rectangle.drawRectangle(drawMode.FILL)       # arg1 - drawMode
triangle.drawTriangle(drawMode.FILL)         # arg1 - drawMode
circle.drawCircle(drawMode.FILL)             # arg1 - drawMode
vertex.drawVertex(True, True, drawMode.FILL) # arg1 - begin, arg2 - end, arg3 - drawMode
polygon.drawPolygon(drawMode.FILL)           # arg1 - drawMode
```

**Important! draw** must be placed in the function specified by **Window** in **winProcess**

For **ALL Primitives**, you need to call the calculateSize function before rendering if you change the value without using the built-in function!

Draw modes:
+ POINTS
+ LOOP
+ FORM
+ FILL
+ RECT
+ LINES

Primitives who may have childrens:
+ Rectangle
+ Triangle
+ Circle

Primitives that have children have features such as:
+ addChild - Add child, arg1 - name, arg2 - Supported primitive;
+ removeChild - Remove child, arg1 - name;
+ getChild - Return child by name, arg1 - name;
+ getChildrens - Return childrens list;

#### Lined
Lined objs have functions such as:
+ setPointSize - setting the line width; (Vec1)
+ setWidthLines - setting the vertex size; (Vec1)
+ setColor - setting the color; (Color3 | Color4)
+ setShader - setting the shader; (Shader)
Lined objs have values such as:
+ color; (Color4, **NOT** Color3)
+ widthlines; (Vec1)
+ pointsize; (Vec1)
+ shader; (Shader)

#### Pointed
Pointed objs have function such as:
+ setPoint1 - settings point1 position; (Vec2)
+ setPoint2 - settings point2 position; (Vec2)
Pointed objs have values such as:
+ point_1; (Vec2)
+ point_2; (Vec2)

#### Line (Lined) (Pointed)
```python
line = Graphics.Line() # arg1 - window (optional)
line.drawLine()
```

#### Arrow (Lined) (Pointed)
```python
arrow = Graphics.Arrow() # arg1 - window (optional)
arrow.drawArrow()
```

#### Parents & Childs
```python
obj1.addChild("Object", obj2) # arg1 - child name, arg2 - another primitive (only Rectangle, Circle, Triangle)
obj1.removeChild("Object")    # arg1 - child name
obj1.getChildrens()           # Return all childrens
obj1.getChild("Object")       # arg1 - child name, return child by name
```

### layerSystem

layerSystem support objects (primitives) such as:
+ Rectangle
+ Triangle
+ Circle
+ Line
+ Arrow
+ Polygon
+ PolygonLegacy
+ Sprite
+ animatedSprite

```python
layers = layerSystem()
layers.addLayer()     # arg1 - layer name (str)
layers.removeLayer()  # arg1 - layer name (str)
layers.addObject()    # arg1 - layer name (str), arg2 - object, arg3 - mode (drawMode | None)
layers.removeObject() # arg1 - layer name (str), arg2 - object, arg3 - mode (drawMode | None)
layers.renderLayers() # Render all layers
```

If you have added an object to a layer, do not draw it separately, because the layers are rendered automatically. For objects that do not support drawMode, set drawMode to None instead.

### Batch

```python
render = batchRender(batchDrawing.STATIC) # batchDrawing (STATIC - for static primitives, add it once. DYNAMIC - for dynamic primitives and are added to update.)
render.addPrimitive(rect)                 # Add primitive (Only Rectangle, Triangle. Textures not supported!!! Don't use draw for batch)
render.setDrawMode(drawMode.FILL)         # Set drawMode for primitives
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
sprite = Sprite(None, None)                 # arg1 - Window, arg2 - Update function
sprite.setPosition(Vec2(0.0, 0.0))          # arg1 - Vec2
sprite.setSize(Vec2(0.0, 0.0))              # arg2 - Vec2
sprite.setColor(Color4(0.0, 0.0, 0.0, 0.0)) # arg1 - Color3 | Color4
sprite.customData.update({"Data":None})     # add custom data
sprite.spriteProcess()                      # Drawing sprite
```

Sprite has values such as:
+ surface; (Rectangle)
+ updateFunction; (function)
+ position; (Vec2)
+ size; (Vec2)
+ color; (Color3 | Color4)
+ customData; (dict)

#### animatedSprite

**animatedSprite** has the same features as **Sprite**.

```python
animation = Animation("Anim", [0, 0], 0.0, None)        # arg1 - Name (str), arg2 - List of frames (ints), arg3 - interval (int | float), arg4 - Loop (bool)

sprite = animatedSprite(None, None)                     # arg1 - Window, arg2 - Update function
sprite.loadFrame("tex", textureType.LINEAR)             # Load texture, arg1 - path, arg2 - textureType
sprite.loadFrames(["tex1", "tex2"], textureType.LINEAR) # Load textures, arg1 - list of paths, arg2 - textureType
sprite.setFrame(0)                                      # Set frame by id, arg1 - id frame
sprite.addAnimation(animation)                          # Add animation, arg1 - Animation
sprite.removeAnimation("Anim")                          # Remove animation, arg1 - Name
sprite.setAnimation("Anim")                             # Sets the animation as current, arg1 - Name
sprite.playAnimation(None)                              # Play setted animation, arg1 - from start (bool)
sprite.stopAnimation()                                  # Stop current animation
```

animatedSprite has values such as:
+ frames; (list)
+ frame; (int)
+ animations; (list)
+ animation; (Animation)
+ animtimer; (Timer)
+ user_update_function; (function)
+ playing; (bool)

#### loadSprite

**loadSprite** has the same features as **Sprite**.

**loadSprite** simply loads the texture when initializing.

```python
sprite = loadSprite(None, None, None) #arg1 - texture path (str), arg2 - texture type (textureType), arg3 - Window, arg4 - Update function
```

### tileMap

```python
tilemap = tileMap(tileMapRender.RECTS, window)                         # arg1 - tileMapRender, arg2 - window
tilemap.setPosition(Vec2(0.0, 0.0))                                    # arg1 - Vec2
tilemap.setTileSize(Vec2(0.0, 0.0))                                    # arg1 - Vec2
tilemap.addTexture(texture, "texture")                                 # arg1 - texture, arg2 - name
tilemap.removeTexture("texture")                                       # arg1 - name
tilemap.addTile(Vec2(0.0, 0.0), "texture", Color3(0.0, 0.0, 0.0, None) # arg1 - position, arg2 - texture name, arg3 - Color (Color3 | Color4), arg4 - skiperrors (bool)
tilemap.removeTile(Vec2(0.0, 0.0), None)                               # arg1 - position, arg2 - skiperrors (bool)
tilemap.drawTileMap(drawMode.FILL)                                     # arg1 - drawMode
```

tileMap has values such as:
+ tiles; (list)
+ tilesize; (Vec2)
+ textures; (list)
+ window; (window)
+ position; (Vec2)
+ batch; (batchRender)

### imgui

**NOTE:** Place any draw function in update function

#### FLAGS:

+ NONE;
+ WINDOW_NO_TITLE_BAR;
+ WINDOW_NO_RESIZE;
+ WINDOW_NO_MOVE;
+ WINDOW_NO_SCROLLBAR;
+ WINDOW_NO_SCROLL_WITH_MOUSE;
+ WINDOW_NO_COLLAPSE;
+ WINDOW_ALWAYS_AUTO_RESIZE;
+ WINDOW_NO_SAVED_SETTINGS;
+ WINDOW_NO_INPUTS;
+ WINDOW_MENU_BAR;
+ WINDOW_HORIZONTAL_SCROLLING_BAR;
+ WINDOW_NO_FOCUS_ON_APPEARING;
+ WINDOW_NO_BRING_TO_FRONT_ON_FOCUS;
+ WINDOW_ALWAYS_VERTICAL_SCROLLBAR;
+ WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR;
+ WINDOW_ALWAYS_USE_WINDOW_PADDING;
+ SELECTABLE_DONT_CLOSE_POPUPS;
+ SELECTABLE_SPAN_ALL_COLUMNS;
+ SELECTABLE_ALLOW_DOUBLE_CLICK;
+ INPUT_TEXT_CHARS_DECIMAL;
+ INPUT_TEXT_CHARS_HEXADECIMAL;
+ INPUT_TEXT_CHARS_UPPERCASE;
+ INPUT_TEXT_CHARS_NO_BLANK;
+ INPUT_TEXT_AUTO_SELECT_ALL;
+ INPUT_TEXT_ENTER_RETURNS_TRUE;
+ INPUT_TEXT_CALLBACK_COMPLETION;
+ INPUT_TEXT_CALLBACK_HISTORY;
+ INPUT_TEXT_CALLBACK_ALWAYS;
+ INPUT_TEXT_CALLBACK_CHAR_FILTER;
+ INPUT_TEXT_ALLOW_TAB_INPUT;
+ INPUT_TEXT_CTRL_ENTER_FOR_NEW_LINE;
+ INPUT_TEXT_NO_HORIZONTAL_SCROLL;
+ INPUT_TEXT_ALWAYS_INSERT_MODE;
+ INPUT_TEXT_READ_ONLY;
+ INPUT_TEXT_PASSWORD;
+ SLIDER_FLAGS_NONE;
+ SLIDER_FLAGS_ALWAYS_CLAMP;
+ SLIDER_FLAGS_LOGARITHMIC;
+ SLIDER_FLAGS_NO_ROUND_TO_FORMAT;
+ SLIDER_FLAGS_NO_INPUT;
+ COMBO_NONE;
+ COMBO_POPUP_ALIGN_LEFT;
+ COMBO_HEIGHT_SMALL;
+ COMBO_HEIGHT_REGULAR;
+ COMBO_HEIGHT_LARGE;
+ COMBO_HEIGHT_LARGEST;
+ COMBO_NO_ARROW_BUTTON;
+ COMBO_NO_PREVIEW;
+ COMBO_HEIGHT_MASK;
+ TAB_BAR_NONE;
+ TAB_BAR_REORDERABLE;
+ TAB_BAR_AUTO_SELECT_NEW_TABS;
+ TAB_BAR_TAB_LIST_POPUP_BUTTON;
+ TAB_BAR_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON;
+ TAB_BAR_NO_TAB_LIST_SCROLLING_BUTTONS;
+ TAB_BAR_NO_TOOLTIP;
+ TAB_BAR_FITTING_POLICY_RESIZE_DOWN;
+ TAB_BAR_FITTING_POLICY_SCROLL;
+ TAB_BAR_FITTING_POLICY_MASK;
+ TAB_BAR_FITTING_POLICY_DEFAULT;
+ TAB_ITEM_NONE;
+ TAB_ITEM_UNSAVED_DOCUMENT;
+ TAB_ITEM_SET_SELECTED;
+ TAB_ITEM_NO_CLOSE_WITH_MIDDLE_MOUSE_BUTTON;
+ TAB_ITEM_NO_PUSH_ID;
+ TAB_ITEM_NO_TOOLTIP;
+ TAB_ITEM_NO_REORDER;
+ TAB_ITEM_LEADING;
+ TAB_ITEM_TRAILING;

##### Use

```python
GUIFlags. # <- FLAG
```

#### Windows

```python
GUIBegin() # Start draw in gui window, arg1 - title (str), arg2 - position (Vec2), arg3 - size (Vec2), arg4 - closable (bool), arg5 - flags (default:0)

GUIEnd()   # End draw
```

```python
GUIBeginChild() # Draw child, arg1 - title (str), arg2 - position (Vec2), arg3 - size (Vec2), arg4 - border (bool), arg5 - flags (default:0)

GUIEndChild()   # End draw
```

#### Widgets

```python
GUIText()    # Draw text in gui window, arg1 - text (str)
GUIButton()  # Draw button in gui window, arg1 - text (str), arg2 - size (Vec2)
GUISButton() # Draw small button in gui window, arg1 - text (str)
GUIIButton() # Draw invisible button in gui window, arg1 - identifier (str), arg2 - size (Vec2), arg3 - flags (default:0)
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

# inputManager
manager = inputManager(window)                   # arg1 - window
manager.kEvent("space", kEvent.Pres)             # Return bool value, if key is pressed - True else False, arg1 - button name (str) USE NAME BUTTON, DON'T Key OR Keys, arg2 - kEvent
manager.mEvent(MouseButton.LEFT, mEvent.Pres)    # Return bool value, if key is pressed - True else False, arg1 - button (MouseButton), arg2 - mEvent
```

inputManager have values such as:
+ active_events; (int)
+ window; (Window)

## Other

### Debugger

```python
debugger = Debugger()
window.connectDebugger(debugger) # Connect debugger, arg1 - Debugger
window.disconnectDebugger()      # Disconnect debugger
debugger.debugDraw(None)         # Draw all objects in LOOP draw mode, arg1 - bool
debugger.showMouseClicks(None)   # Show Pressed, Released, Position cursor and  arrow from 1 point to 2 point, arg1 - bool
```

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

### generateID

```python
generateID() # Return int, generate unique ID
```

### Tween

```python
tween = Tween(0.0, 0.0, 0.0, None, tweenType.LINEAR) # arg1 - start point (float | int), arg2 - end point (float | int), arg3 - duration (float | int), arg4 - callback, arg5 - tweenType
tween.tweenProcess()                                 # Place in update
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

## Physics

### Collision

#### AABBCollision

```python
if checkCollision(rect1.vertexes, rect2.vertexes):
    print("Colliding")
```

**OR**

```python
if AABBCollision(rect1.vertexes, rect2.vertexes):
    print("Colliding")
```

#### SATCollision

```python
if SATCollision(rect1.vertexes, rect2.vertexes):
    print("Colliding")
```

#### GlobalAABBCollision

```python
if GlobalAABBCollision(rect1):
    print("Colliding")
```

#### GlobalSATCollision

```python
if GlobalSATCollision(rect1):
    print("Colliding")
```

#### Globals collision note!

Use Global's collision after all draw!

#### rayCast

```python
raycast = rayCast()                                  # arg1 - list of ignores bodyes
raycast.setPositions(Vec2(0.0, 0.0), Vec2(0.0, 0.0)) # arg1 - first pos (Vec2), arg2 - second pos (Vec2)
raycast.rayCastProcess()                             # A function that checks whether a raycast encounters an object
raycast.rayCastDraw()                                # A function that renders raycast as a line
```

rayCast has values such as:
+ pos1 - Vec2;
+ pos2 - Vec2;
+ ignores - List;
+ colliding - bool;

## Math

### Clamp

```python
Math.Clamp(x, y, value) # Limits the number, arg1 - minimum, arg2 - maximum, arg3 - current value. All values is float|int
```

### clampVec2

```python
Math.clampVec2(x, y, vector) # Limits Vec2 on two axes at once, arg1 - minimum (float|int), arg2 - maximum (float|int), arg3 - Vec2
```

### getDistanceVec2

```python
Math.getDistanceVec2(x, y) # Get distance, arg1 - first vector (Vec2), arg2 - second vector (Vec2)
```

### Lerp

```python
lerp = Math.Lerp(0.0, 0.0, 0.0) # arg1 - Start pos (int | float), arg2 - End pos (int | float), arg3 - time (int | float)
```

### Random

#### randomNum

```python
random_float = randomNum(0.0, 0.0) # Return random float, arg1 - float, arg2 - float
random_int = randomNum(0, 0)       # Return random int, arg1 - int, arg2 - int
```

#### randomBool

```python
random_bool = randomBool() # Return True or False
```

#### randomChoce

```python
random_choice = randomChoice(list) # Return random element in list
```

## Modules

### All module use

```python
obj.connectModule(module)
obj.runModuleFunction("module", "function", args) # arg1 - module name, arg2 - function name, arg3-inf - args
obj.setModuleValue("module", "value", your_value) # arg1 - module name, arg2 - value name, arg3 - value
obj.getModuleValue("module", "value")             # arg1 - module name, arg2 - value name
```

### collider4Body

Use:

```python
obj.connectModule(collider4Body())
```

collider4Body() has function such as:
+ getColliding - Return if body colliding with other body, use after all drawing, arg1 - side, sides: 1 - top, 2 - bottom, 3 - left, 4 - ;right
collider4Body() has values such as:
+ showcolliders (bool);
+ colliders (list 4 Rectangles);
+ current_body (any);
+ top (Rectangle);
+ bottom (Rectangle);
+ left (Rectangle);
+ right (Rectangle);

### How to create my own module

```python
class yourModule:
    def __init__(self):
        pass

    def _inited(self):
        # <- YOUR INIT CODE HERE
        pass

    def _work(self, body): # BODY THIS IS RECTANGLE, TRIANGLE OR CIRCLE
        # <- YOUR CODE HERE (UPDATE CODE WITH WINDOW)
        pass
```

## Direct import

You can use libraries like glfw and PyOpenGL right in the game, just use:

```python
OpenGL
glfw
imgui
```

**OpenGL is a GL from the PyOpenGL library!**

## Problems

### Import in engine

#### batchRender

If you are using a version prior to the 26.1.1.7R release, there may be problems with importing **batchRender**. Solution:

Open __init__.py in folder Engine and edit:

```python

# BEFORE:

from .Graphics.Render.batchrender import batchRender

# AFTER:

from .Graphics.Render.batchRender import batchRender
```

### Render

#### If you can't see anything

Some graphics objects cannot be drawn in the new render. Solution:

```python

# BEFORE:

window = Window(0)

# AFTER

window = Window()
```

## Debug

```
setDebug(False) # on/off debug, True - log in chat, False - disable log in chat
```

### F12 Debug

Press F12 to open debug menu

```python
window.setLegacyDebug(True) # Set old debug, arg1 - bool
```

<p align="center">OLD:</p>

![Old](https://i.ibb.co/21PXC9Hm/old.png)

<p align="center">NEW:</p>

![New](https://i.ibb.co/GfV0tJnP/new.png)

## Note

See [examples](Examples)
