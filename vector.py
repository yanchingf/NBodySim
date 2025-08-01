
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return ("Vector({}, {}, {})".format(self.x,self.y,self.z))
    

    # getters
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z
    
    # setters

    def setX(self, a):
        self.x = a
    def setY(self, a):
        self.y = a
    def setZ(self, a):
        self.z = a


    # vector math

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

