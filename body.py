
from vector import Vector
import matplotlib.pyplot as plt
import math
import itertools
import constants

class Body:

    display_size = 10
    display_log_base = 1.3

    def __init__(self, mass, system, position = (0,0,0), velocity = Vector(0,0,0), color="white"):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.system = system
        self.color = color

        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.display_size,
        )
    
    def move(self):
        self.position =  (
            self.position[0] + self.velocity.getX(),
            self.position[1] + self.velocity.getY(),
            self.position[2] + self.velocity.getZ(),
        )

    def accelerate(self, b2):

        pos_v1 = Vector(self.position[0],
                        self.position[1],
                        self.position[2])
        
        pos_v2 = Vector(b2.position[0], 
                        b2.position[1], 
                        b2.position[2])


        distance = pos_v1.subtract(pos_v2)

        print(pos_v1)
        print(pos_v2)

        print(distance)

        radius_sq = distance.get_magnitude() ** 2

        force_mag = (self.mass * b2.mass) / (radius_sq)
        force = distance.normalize().multiply(force_mag)

        a1 = force / self.mass
        a2 = -force / b2.mass

        self.velocity =  a1 
        b2.velocity += a2

    def draw(self):
        self.system.axes.plot(
            *self.position,
            marker = "o",
            markersize=self.display_size,
            color=self.color,
        )

    def __str__(self):
        return ("Position: ({}, {}, {}, \n Velocity: ({}, {}, {}), \n Mass : {} \n").format(
            self.position[0], self.position[1], self.position[2],
            self.velocity.getX(), self.velocity.getY(), self.velocity.getZ(),
            self.mass
        )


