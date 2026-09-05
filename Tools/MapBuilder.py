from tkinter.filedialog import askopenfilename
from OpenGameEngine import *
import json

window = Renderer.Window(use_gl_im=False)
window.SetTitle("Map Builder")
window.SetVSync(0)

camera = Renderer.Camera3D()
window.SetCamera(camera)

objects = []
last_object = 0

selected_obj = None
selected_obj_params = [Vec3(0, 0, 0), Vec3(1, 1, 1), Color4(1, 1, 1, 1), Vec3(0, 0, 0)]

def SaveMap():
    objects_lists = []

    for obj in objects:
        if isinstance(obj[0], gfx.Cube):
            pos = obj[0].position
            size = obj[0].size
            rot = obj[0].rotation
            color = obj[0].color
            name = obj[1]
            objects_lists.append([
                0, 
                f"{name}",
                float(pos.x), float(pos.y), float(pos.z),
                float(size.x), float(size.y), float(size.z),
                float(rot.x), float(rot.y), float(rot.z),
                float(color.r), float(color.g), float(color.b), float(color.a)
            ])

    output = {
        "ResID":0,
        "Data":{
            "Objects":objects_lists,
            "LastObject":last_object
        }
    }

    with open("OutputMap.res", "w+") as f:
        json.dump(output, f, indent=4)

def LoadMap():
    global objects, last_object, selected_obj

    filepath = askopenfilename(filetypes=[["Resource", ".res"]])

    if not filepath:
        return
    
    with open(filepath, "r") as f:
        data = json.load(f)

    if data["ResID"] != 0:
        return

    objects = []

    for obj in data["Data"]["Objects"]:
        if obj[0] == 0:
            cube = gfx.Cube()
            Transform.SetPosition(cube, Vec3(obj[2], obj[3], obj[4]))
            Transform.SetSize(cube, Vec3(obj[5], obj[6], obj[7]))
            Transform.SetRotation(cube, Vec3(obj[8], obj[9], obj[10]))
            Color.Set(cube, Color4(obj[11], obj[12], obj[13], obj[14]))
            objects.append([cube, obj[1]])

    last_object = data["Data"]["LastObject"]

    selected_obj = None

def AddCube():
    global last_object

    name = f"Object{last_object}"

    cube = gfx.Cube()
    Transform.SetSize(cube, Vec3(1, 1, 1))
    Color.Set(cube, Color3(1, 1, 1))
    
    objects.append([cube, name])

    last_object += 1

def RemoveObj():
    global selected_obj

    objects.remove(selected_obj)

    selected_obj = None

def Render():
    for obj in objects:
        obj[0].Draw()

def DrawGui():
    global selected_obj, selected_obj_params

    with ImGUI.Begin("Tree", Vec2(5, 5), Vec2(180, 200), flags=Renderer.GUI.Flags.WINDOW_NO_MOVE | Renderer.GUI.Flags.WINDOW_NO_RESIZE):
        _add_cube = ImGUI.Button("Add Cube", Vec2(-1, 0))

        if _add_cube:
            AddCube()

        with ImGUI.BeginChild("Objects:"):
            for index, obj in enumerate(objects):
                if ImGUI.Button(f"{obj[1]}##ObjectInTree{index}", Vec2(-1, 0)):
                    selected_obj = obj

                    pos = selected_obj[0].position
                    size = selected_obj[0].size
                    rot = selected_obj[0].rotation
                    color = selected_obj[0].color
                    selected_obj_params = [pos, size, color, rot]
    
    with ImGUI.Begin("Inspector", Vec2(5, 225), Vec2(180, 200), flags=Renderer.GUI.Flags.WINDOW_NO_MOVE):
        if selected_obj:
            ImGUI.Label(f"{selected_obj[1]}")

            pos = selected_obj_params[0]
            size = selected_obj_params[1]
            color = selected_obj_params[2]
            rot = selected_obj_params[3]

            ImGUI.Label("Position:")
            _, PX = ImGUI.InputText("X##IP", str(pos.x))
            _, PY = ImGUI.InputText("Y##IP", str(pos.y))
            _, PZ = ImGUI.InputText("Z##IP", str(pos.z))

            ImGUI.Label("Size:")
            _, SX = ImGUI.InputText("X##IS", str(size.x))
            _, SY = ImGUI.InputText("Y##IS", str(size.y))
            _, SZ = ImGUI.InputText("Z##IS", str(size.z))

            ImGUI.Label("Rotation:")
            _, RX = ImGUI.InputText("X##IR", str(rot.x))
            _, RY = ImGUI.InputText("Y##IR", str(rot.y))
            _, RZ = ImGUI.InputText("Z##IR", str(rot.z))

            ImGUI.Label("Color:")
            _, CR = ImGUI.InputText("R##IC", str(color.r))
            _, CG = ImGUI.InputText("G##IC", str(color.g))
            _, CB = ImGUI.InputText("B##IC", str(color.b))
            _, CA = ImGUI.InputText("A##IC", str(color.a))

            if ImGUI.Button("Remove", Vec2(-1, 0)):
                RemoveObj()

            try:
                selected_obj_params = [Vec3(float(PX), float(PY), float(PZ)), Vec3(float(SX), float(SY), float(SZ)), Color4(float(CR), float(CG), float(CB), float(CA)), Vec3(float(RX), float(RY), float (RZ))]
                pos = selected_obj_params[0]
                size = selected_obj_params[1]
                color = selected_obj_params[2]
                rot = selected_obj_params[3]
                Transform.SetPosition(selected_obj[0], pos)
                Transform.SetSize(selected_obj[0], size)
                Transform.SetRotation(selected_obj[0], rot)
                Color.Set(selected_obj[0], color)
            except:...

    with ImGUI.Begin("Tools", Vec2(190, 5), Vec2(360, 60), flags=Renderer.GUI.Flags.WINDOW_NO_MOVE | Renderer.GUI.Flags.WINDOW_NO_RESIZE):
        if ImGUI.Button("Save"):
            SaveMap()
        ImGUI.SameLine()
        if ImGUI.Button("Load"):
            LoadMap()

def Movement():
    dt = window.GetDelta()

    if Input.Keyboard.KeyPressed(Keys.A):
        camera.MoveRight(-2*dt)
    elif Input.Keyboard.KeyPressed(Keys.D):
        camera.MoveRight(2*dt)

    if Input.Keyboard.KeyPressed(Keys.W):
        camera.MoveForward(2*dt)
    elif Input.Keyboard.KeyPressed(Keys.S):
        camera.MoveForward(-2*dt)

    if Input.Keyboard.KeyPressed(Keys.LEFT_SHIFT):
        camera.position.y += 2*dt
    elif Input.Keyboard.KeyPressed(Keys.LEFT_CONTROL):
        camera.position.y -= 2*dt

    if Input.Keyboard.KeyPressed(Keys.E):
        camera.yaw += 128*dt
    elif Input.Keyboard.KeyPressed(Keys.Q):
        camera.yaw -= 128*dt

@window.UpdateFunction
def Update():
    DrawGui()
    Render()
    Movement()

window.Run()