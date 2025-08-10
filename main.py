
from system import System
from body import Body
from vector import Vector
from constants import Constants


sys = System(400)

# why are they leaving 💔

b1 = Body(20, sys, color="red", position = Vector(150,50,0), velocity=Vector(0, 0, 5))
b2 = Body(1000, sys, color="blue", position = Vector(100,-50,150), velocity=Vector(5,0, 0))

sys.addBody(b1)
sys.addBody(b2)

while (1 > 0):
    sys.calculateAllInteractions()
    sys.updateBodies()
    sys.drawAll()

    print("velocity 1: {}".format(b1.velocity))
    print("position 1: {}".format(b1.position))

    print("velocity 2: {}".format(b2.velocity))
    print("position 2: {}".format(b2.position))
