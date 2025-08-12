#system.py

from vector import Vector
from body import Body
import matplotlib.pyplot as plt
import math
import itertools
import constants

plt.style.use('dark_background')

class System:

    def __init__(self, size):
        self.size = size
        self.bodies = []

        self.fig, self.axes = plt.subplots(
            1,
            1,
            subplot_kw={"projection": "3d"},
            figsize=(self.size / 50, self.size / 50),
        )
        self.fig.tight_layout()

    
    def addBody(self, b):
        self.bodies.append(b)


    def updateBodies(self):
        self.bodies.sort(key=lambda item: item.position.x)
        for b in self.bodies:
            b.move()
            b.draw()


    def drawAll(self):

        self.axes.set_xlim((-self.size/2, self.size/2))
        self.axes.set_ylim((-self.size/2, self.size/2))
        self.axes.set_zlim((-self.size/2, self.size/2))

        # self.axes.axis(False)

        plt.pause(.0001)
        self.axes.clear()

        

    def calculateAllInteractions(self):

        s = len(self.bodies)

        for i in range(s):
            for i2 in range(s):
                if (i != i2):
                    self.bodies[i].accelerate(self.bodies[i2])
                






