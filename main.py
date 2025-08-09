
from system import System
from body import Body
from vector import Vector
from constants import Constants


sys = System(400)
# def __init__(self, mass, system, position = (0,0,0), velocity = Vector(0,0,0), color="white"):
b1 = Body(100, sys, color="red", position = (1,1,1))
b2 = Body(100, sys, color="blue", position = (0,0,0))
b3 = Body(100, sys, color="blue", position = (-1,-1,-1))

sys.addBody(b1)
sys.addBody(b2)
sys.addBody(b3)

while (1 > 0):
    sys.calculateAllInteractions()
    sys.updateBodies()
    sys.drawAll()