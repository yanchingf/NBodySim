
from vector import Vector

class Particle:

    def __init__(self, position, mass):
        self.position = position
        self.prev_position = position.copy()
        self.velocity 
        self.acceleration
        self.mass = mass

    def update(self, dt):
        self.position.add(self.velocity).multiply(dt)
        self.velocity.add(self.acceleration).multiply(dt)
        self.acceleration = Vector(0, 0, 0)