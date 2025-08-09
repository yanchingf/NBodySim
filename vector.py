
import math

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return ("Vector({}, {}, {})".format(self.x,self.y,self.z))

    def add(self, v2):
        return Vector(
            x = self.x + v2.x,
            y = self.y + v2.y,
            z = self.z + v2.z
        ) 
    def subtract(self, v2):
        return Vector(
            x = self.x - v2.x,
            y = self.y - v2.y,
            z = self.z - v2.z
        )
    def multiply(self, a):
        return Vector(
            x = self.x * a,
            y = self.y * a,
            z = self.z * a
        )
    def divide(self, a):
        return Vector(
            x = self.x / a,
            y = self.y / a,
            z = self.z / a
        )

    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def normalize(self):
        m = self.get_magnitude()
        return Vector(
            x = self.x / m,
            y = self.y / m,
            z = self.z / m
        )



