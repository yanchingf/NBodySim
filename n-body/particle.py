
from vector import Vector
from constants import Constants

c = Constants()

class Particle:

    def __init__(self, mass = 1, position = Vector(0,0)):

        self.position = position
        self.prev_position = position.copy()

        self.velocity = Vector(0,0)
        self.acceleration = Vector(0,0)

        self.mass = mass

    def move(self):
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y

    def accelerate(self, b2):

        distance = b2.position.subtract(self.position)

        r_sq = distance.get_magnitude() ** 2 

        force_mag = (self.mass * b2.mass) / (r_sq) 
        force = distance.normalize().multiply(force_mag)

        a1 = force.divide(self.mass).multiply(c.G)
        a2 = force.divide(b2.mass).multiply(c.G)

        self.velocity = self.velocity.add(a1)
        b2.velocity = b2.velocity.subtract(a2)

