# Import

Rename the downloaded folder if its name is not "OpenGameEngine"

```python
from OpenGameEngine import *
```

# Vectors

```python
Vector1 = Vec1(0.0)
Vector2 = Vec2(0.0, 0.0)
Vector3 = Vec3(0.0, 0.0, 0.0)
```

You can:
+ Vec1 + Vec1
+ Vec1 - Vec1
+ Vec1 * Vec1
+ Vec1 * N
+ Vec1 / Vec1
+ Vec1 / N

+ Vec2 + Vec2
+ Vec2 - Vec2
+ Vec2 * Vec2
+ Vec2 * N
+ Vec2 / Vec2
+ Vec2 / N

+ Vec3 + Vec3
+ Vec3 - Vec3
+ Vec3 * Vec3
+ Vec3 * N
+ Vec3 / Vec3
+ Vec3 / N

Vectors accept int or float

Vec1 has values such as: x
Vec2 has values such as: x, y
Vec3 has values such as: x, y, z

# Colors

```python
Color3(0.0, 0.0, 0.0)
Color4(0.0, 0.0, 0.0, 0.0)
```

Colors accept int ot float
Color value 0-1

Color3 has values such as: r, g, b
Color4 has values such as: r, g, b, a

```python
c256(0.5) # Convert 0-256 to 0-1, return float, arg1 - x (float or int)
```

# Graphical

TextureFilter has:
+ NEAREST
+ LINEAR

# Renderer

# NOTE

**3D** render in **NDC**
**2D** render in **px**

## Window

```python
window = Renderer.Window()
window.SetTitle("Window")      # arg1 - Title (str)
window.SetSize(Vec2(640, 480)) # arg1 - Size (Vec2)
window.SetVSync(0)             # if 1 - vsync enabled, if 0 - vsync - disabled, arg1 - sync (int) (default: 1)     
window.GetFPS()                # Return FPS
window.GetDelta()              # Return Delta time

@window.UpdateFunction         # Pointer for update function
def update():
	pass                       # <- Your update code here

window.Run()                   # Start main loop
```

## Cameras

You must have a camera for your game!

### Camera2D

```python
camera2d = Renderer.Camera2D()
window.SetCamera(camera2d)
```

Camera2D has values such as:
+ position (Vec2)
+ zoom (float)

**Zoom bad working**

Pivot: top-left

### Camera3D

```python
camera3d = Renderer.Camera3D()
window.SetCamera(camera3d)
```

Camera3D has values such as:
+ position (Vec3)
+ fov (float)
+ pitch (float)
+ yaw (float)

Camera3D has methods such as:
+ MoveForward, arg1 - Distance (int | float)
+ MoveRight, arg1 - Distance (int | float)

## GL_IM

If you want to disable this feature, when initializing the window, set the argument "use_gl_im" to (bool). By default, it is True.

```python
Renderer.Window(use_gl_im=False)
```

**This rendering method must be executed in a loop.** This mode merely simulates the old one.

```python
glBegin()    # Method for start draw
glEnd()      # Method for end draw
glVertex2f() # Place Vertex, arg1 - posx (float), arg2 - posy (float)
glColor3f()  # Setup Color3 for next vertices, arg1 - r (float), arg2 - g (float), arg3 - b (float)
glColor4f()  # Setup Color4 for next vertcies, arg1 - r (float), arg2 - g (float), arg3 - b (float), arg3 = a (float)
```

## Materials

If you want to disable this feature, when initializing the window, set the argument "use_materials" to (bool). By default, it is True.

```python
Renderer.Window(use_materials=False)
```

```python
material = Material3D() # Create material
Material.Set()          # Set Material3D for Object, arg1 - Object, arg2 - Material (Material3D)
```

Material3D has values such as:
+ ambient_color - Color3
+ light_pos - Vec2
+ light_color - Color3
+ texture - Texture
+ color - Color4

# Primitives

Primitives has function such as:
+ Draw - Place in update function for drawing

## 2D

```python
rectangle = gfx.Rectangle()
triangle = gfx.Triangle()
circle = gfx.Circle() # arg1 - s (Segments, Default:32, optional)
```

Pivot: top-left

## 3D

```python
quad = gfx.Quad()
cube = gfx.Cube()
```

Pivot: center

# Transform

```python
Transform.SetPosition() # arg1 - Object (Primitive), arg2 - Position (Vec2 - for 2D, Vec3 - for 3D)
Transform.SetSize()     # arg1 - Object (Primitive), arg2 - Size (Vec2 - for 2D, Vec3 - for 3D)
Transform.SetRotation() # arg1 - Object (Primitive), arg2 - Rotation (Vec1 - for 2D, Vec3 - for 3D)
Transform.Move()        # arg1 - Object (Primitive), arg2 - Position (Vec2 - for 2D, Vec3 - for 3D)
Transform.Scale()       # arg1 - Object (Primitive), arg2 - Size (Vec2 - for 2D, Vec3 - for 3D)
Transform.Rotate()      # arg1 - Object (Primitive), arg2 - Rotation (Vec1 - for 2D, Vec3 - for 3D)

Transform.GetPosition() # Return Vec2 or Vec3, arg1 - Object (Primitive)
Transform.GetSize()     # Return Vec2 or Vec3, arg1 - Object (Primitive)
```

# Color

```python
Color.Set()           # arg1 - Object (Primitive), arg2 - Color (Color3 Or Color4)
Color.SetBackGround() # arg1 - Color (Color3 or Color4)
```

Default BGColor: 0.1, 0.1, 0.1

**DON'T PLACE SetBackGround IN UPDATE**

# Textures

```python
texture_raw = Renderer.TextureReader() # Return raw texture, arg1 - path (str)
texture = Renderer.TextureLoader()     # Return texture, arg1 - texture_raw (str), arg2 - _filter (TextureFilter)
Texture.Set()                          # Set texture, arg1 - Object, arg2 - Texture 
```

## UV

```python
Texture.SetUV() # Set UV, arg1 - Object, arg2 - UV (list of vec2s, count = number of vertices)
```

It's better not to edit the UVs of the circle (since there are a lot of UV points there)

Mini example:

```python
Texture.SetUV(..., [Vec2(0, 0), Vec2(1, 0), Vec2(1, 1), Vec2(0, 1)]) # Working for only rectangle
```

**UV Made Automatic!**

# Layers

```python
Layers.Set() # arg1 - Object, arg2 - Layer (int)
Layers.Get() # Return int, arg1 - Object
```

## In engine textures

See [Textures names](Textures.md)

```python
texture_path = textures.Get() # Return texture path, arg1 - name
```

# Input

## Keyboard

See [Keys](Keys.md)

```python
Input.Keyboard.KeyPressed(Keys.SPACE)            # Return bool
Input.Keyboard.KeyJustPressed(Keys.SPACE)        # Return bool
Input.Keyboard.ConnectCallback(func, Keys.SPACE) # Connect callback, no in function args
```

## Mouse

See [MouseButtons](MouseButtons.md)

```python
Input.Mouse.GetPosition()                      # Return Vec2
Input.Mouse.MouseKeyPressed(MouseButton.LEFT)  # Return bool, arg1 - Button (MouseButton)
Input.Mouse.MouseKeyReleased(MouseButton.LEFT) # Return bool, arg1 - Button (MouseButton)
```

# Math

## Math

**Note:** X - minimum, Y - maximum in Clamps

```python
Math.Clamp()           # Return clamped value, arg1 - x (int or float), arg2 - y (int or float), arg3 - value (int or float)
Math.ClampVec2()       # Return clamped Vec2, arg1 - x (int or float), arg2 - y (int or float), arg3 - value (int or float)
Math.ClampVec3()       # Return clamped Vec3, arg1 - x (int or float), arg2 - y (int or float), arg3 - value (int or float)
Math.GetDistanceVec2() # Return distance between Vec2's, arg1 - x (Vec2), arg2 - y (Vec2)
Math.Lerp()            # Return float, arg1 - a (int or float), arg2 - b (int or float), arg3 - t (int or float)
```

## Random

```python
Random.RandomNum()    # Return flot if all args is flaot, return int if all args is int, arg1 - x (int or float), arg2 - (int or float)
Random.RandomBool()   # Return bool, True or False
Random.RandomChoice() # Return random element in list, arg1 - x (list)
Random.RandomColor3() # Return random Color3
Random.RandomColor4() # Return random Color4, arg1 - rnd_alpha (bool) (default - False)
```

# Misc

## Timer

```python
timer = Misc.Timer() # arg1 - target_sec (int), func (default - None)
timer.Process()      # Place in update function
```

## Scenes

```python
class Scene(Misc.SceneClass):
	def SceneI(self):
		pass # <- Your init code here

	def SceneU(self):
		pass # <- Your update code here

scenes = Misc.SceneManager()
scenes.AddScene()   # arg1 - scene (scene class), arg2 - name (str)
scenes.SetScene()   # arg1 - name (str)
scenes.UnSetScene()
scenes.Process()    # Place in update function
```

## ResourceLoader

```python
resources = Misc.ResourceLoader() # arg - path (str), arg2 - files (tuple)
```

Mini example:
```python
resources = Misc.ResourceLoader("files", (("*.png", Misc.ResourceType.TEXTURE_NEAREST), ("*.wav", Misc.ResourceType.AUDIO)))
```

ResourceTypes:
+ TEXTURE_LINEAR
+ TEXTURE_NEAREST
+ AUDIO

## IDGen

```python
id0 = Misc.IDGen()
id1 = Misc.IDGen()
id2 = Misc.IDGen()
```

Generates a unique ID

# Physics

## Collision

```python
colliding = Physics.BoxCollision(rect1, rect2) # arg1 - rect1 (Rectangle), arg2 - rect2 (Rectangle)
```

# Audio

```python
audio_raw = sfx.AudioLoader() # Return raw audio, arg1 - audio_path (str)
audio = Audio()               # Make audio class
audio.SetSource()             # arg1 - source (audio raw)
audio.Play()                  # Audio play
audio.Stop()                  # Audio stop
audio.SetPosition()           # arg1 - position (float, 0-1)
audio.IsPlaying()             # Return bool, you can use without ()
```

# Debug

Press F12 to open debug menu

```python
DisableDebug() # Remove all DINF, DWAR, DERR
```
