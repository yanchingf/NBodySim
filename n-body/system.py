
import math
from particle import Particle
from constants import Constants
from barneshut import Node

c = Constants()

class System:

    def __init__(self, n=100, m=10):

        self.bodies[n] = []
        self.root = Node(0, 0, c.bound)

    def gravitateAll(self, other):

        for i, b1 in enumerate(self.bodies[0:len(self.bodies)-1]):
            for j, b2 in enumerate(self.bodies[1:len(self.bodies)]):
                b1.accelerate(b2)

    
    # traverse tree, if s/d < tolerance then continue to next node
    # s width of node, d dist between body and cofm of other
    def updateForce(self, particle, curr):

        d = math.sqrt((particle.position.x - curr.com_pos.x)**2 + (particle.position.y - curr.com_pos.y)**2)

        if ((curr.bound / d) < c.quad_tolerance):
            return 

        else:
            if (len(curr.children) == 0):
                return 

            else:
                for child in children:
                    calculateForce(particle, child)


    def calculateForce(self):
        return # todo


        
        




            

      


    
            


    


    
