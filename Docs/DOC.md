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

### Camera2D

```python
camera2d = Renderer.Camera2D()
window.SetCamera(camera)
```

Camera2D has values such as:
+ position (Vec2)
+ zoom (float)

**Zoom bad working**

# Primitives

```python
rectangle = gfx.Rectangle()
triangle = gfx.Triangle()
```

Primitives has function such as:
+ Draw - Place in update function for drawing

# Transform

```python
Transform.SetPosition() # arg1 - Object (Primitive), arg2 - Position (Vec2 - for 2D, Vec3 - for 3D)
Transform.SetSize()     # arg1 - Object (Primitive), arg2 - Size (Vec2 - for 2D, Vec3 - for 3D)
Transform.Move()        # arg1 - Object (Primitive), arg2 - Position (Vec2 - for 2D, Vec3 - for 3D)
Transform.Scale()       # arg1 - Object (Primitive), arg2 - Size (Vec2 - for 2D, Vec3 - for 3D)
```

# Color

```python
Color.Set() # arg1 - Object (Primitive), arg2 - Color (Color3 Or Color4)
```

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

Mini example:

```python
Texture.SetUV(..., [Vec2(0, 0), Vec2(1, 0), Vec2(1, 1), Vec2(0, 1)]) # Working for only rectangle
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
