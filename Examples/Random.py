import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from OpenGameEngine import *

window = Window()
window.initWindow()

l = [1, 2, 3, 4, 5, 6]

print(f"Random int:{Random.randomNum(0, 10)}")
print(f"Random float:{Random.randomNum(0.0, 10.0)}")
print(f"Random bool:{Random.randomBool()}")
print(f"Random choice:{Random.randomChoice(l)}")

window.winProcess()