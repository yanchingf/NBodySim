#system.py

from vector import Vector
import matplotlib.pyplot as plt
import math

plt.style.use('dark_background')

class System:

    def __init__(self, size):
        self.size = size
        self.bodies = []

        self.fig, self.axes = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size/50, self.size/50),
        )
        self.fig.tight_layout()
    
    def addBody(self, b):
        self.bodies.append(b)

    def updateBodies(self):
        for b in self.bodies:
            b.move()
            b.draw()

    def drawAll(self):
        self.axes.set_xlim((-self.size/2, self.size/2))
        self.axes.set_ylim((-self.size/2, self.size/2))
        self.axes.set_zlim((-self.size/2, self.size/2))

        plt.pause(0.0001)
        self.axes.clear()


class Body:

    display_size = 10
    display_log_base = 1.3

    def __init__(self, mass, system, position = (0,0,0), velocity = Vector(0,0,0), color="black"):
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


test = System(400)
t_body = Body(100, test, velocity=Vector(1, 1, 1))
test.addBody(t_body)

print(t_body)

for _ in range(100):
    test.updateBodies()
    test.drawAll()
