
from system import System
from body import Body
from vector import Vector
from constants import Constants

c = Constants()
sys = System(400)

# why are they leaving 💔

b1 = Body(20, sys, color= "red", position = Vector(100, -50, 150), velocity=Vector(5, 0, 0))
b2 = Body(10, sys, color= "blue", position = Vector(150, 50 ,0), velocity=Vector(0, 5, 5))
b3 = Body(100000, sys, color= "yellow", position = Vector(0,0,0), velocity=Vector(0, 0, 0))

sys.addBody(b1)
sys.addBody(b2)
sys.addBody(b3)

for i in range(300):
    sys.calculateAllInteractions()
    sys.updateBodies()
    sys.drawAll()
