
import math
from particle import Particle
from constants import Constants

c = Constants()

class System:
    def __init__(self, n=100, m=10):
        self.bodies[n]


    def gravitate(self, other):

        dist = other.position.minus(self.position)
        dist_mag = dist.get_magnitude() 

        # G * (m_1 * m_2) / d^2
        force_mag = (self.mass * other.mass) * c.G / (dist_mag**2 + c.softening)
        force = dist.divide(dist_mag).multiply(force_mag)
                
        # F/m = a
        self.acceleration = self.acceleration.add(force.divide(other.mass))
        other.acceleration = self.acceleration.subtract(force.divide(self.mass))


    
