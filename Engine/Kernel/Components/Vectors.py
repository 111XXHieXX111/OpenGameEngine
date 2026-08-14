class Vec2:
    __slots__ = ("x", "y")
    
    def __init__(self, x:int | float, y:int | float):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vec2(self.x * scalar, self.y * scalar)
        elif isinstance(scalar, Vec2):
            return Vec2(self.x * scalar.x, self.y * scalar.y)
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vec2(self.x / scalar, self.y / scalar)
        elif isinstance(scalar, Vec2):
            return Vec2(self.x / scalar.x, self.y / scalar.y)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

class Vec1:
    __slots__ = ("x",)
    
    def __init__(self, x:int | float):
        self.x = x

    def __add__(self, other):
        return Vec1(self.x + other.x)
    
    def __sub__(self, other):
        return Vec1(self.x - other.x)
    
    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vec1(self.x * scalar)
        elif isinstance(scalar, Vec1):
            return Vec1(self.x * scalar.x)
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vec1(self.x / scalar)
        elif isinstance(scalar, Vec1):
            return Vec1(self.x / scalar.x)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

class Vec3:
    __slots__ = ("x", "y", "z")

    def __init__(self, x:int | float, y:int | float, z:int | float):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)
        elif isinstance(scalar, Vec3):
            return Vec3(self.x * scalar.x, self.y * scalar.y, self.z * scalar.z)
    
    def __truediv__(self, scalar):
        if isinstance(scalar, (int, float)):
            return Vec3(self.x / scalar, self.y / scalar, self.z / scalar)
        elif isinstance(scalar, Vec3):
            return Vec3(self.x / scalar.x, self.y / scalar.y, self.z / scalar.z)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)
