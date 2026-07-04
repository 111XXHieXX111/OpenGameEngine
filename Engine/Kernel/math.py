PI = 3.141592

def sin(x):
    x = x % (2 * PI)
    if x > PI:
        x -= 2 * PI
    
    result = 0
    term = x
    for n in range(10):
        result += term
        term = term * (-x * x) / ((2*n + 2) * (2*n + 3))
    return result

def cos(x):
    x = x % (2 * PI)
    if x > PI:
        x -= 2 * PI
    
    result = 0
    term = 1
    for n in range(10):
        result += term
        term = term * (-x * x) / ((2*n + 1) * (2*n + 2))
    return result

def radians(degrees):
    return degrees * PI / 180
