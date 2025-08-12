
from vector import Vector
import matplotlib.pyplot as plt
import math
import itertools
from constants import Constants

c = Constants()

class Body:

    display_size = 10
    display_log_base = 1.3

    def __init__(self, mass, system, position = Vector(0,0,0), velocity = Vector(0,0,0), color="white"):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.system = system
        self.color = color

        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.display_size,
        )

    def pos_as_iter(self):
        return (self.position.x, self.position.y, self.position.z)
    
    def move(self):
        self.position =  Vector(
            self.position.x + self.velocity.x,
            self.position.y + self.velocity.y,
            self.position.z + self.velocity.z
        )

    def accelerate(self, b2):

        distance = b2.position.subtract(self.position).add(Vector(c.bound,c.bound,c.bound))

        r_sq = distance.get_magnitude() ** 2 

        force_mag = (self.mass * b2.mass) / (r_sq) 
        force = distance.normalize().multiply(force_mag)

        a1 = force.divide(self.mass).multiply(c.G)
        a2 = force.divide(b2.mass).multiply(c.G)

        self.velocity = self.velocity.add(a1)
        b2.velocity = b2.velocity.subtract(a2)

        


    def draw(self):
        pos_t = self.pos_as_iter()
        self.system.axes.plot(
            pos_t[0],
            pos_t[1],
            pos_t[2],
            marker = "o",
            markersize=self.display_size,
            color=self.color,
        )


    def __str__(self):
        return ("Position: {}, \n Velocity: {}, \n Mass : {} \n").format(
            self.position,
            self.velocity,
            self.mass
        )
    


