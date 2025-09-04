
import numpy as np
import matplotlib as plt
from matplotlib import pyplot
from matplotlib import animation
from vector import Vector
from constants import Constants
from particle import Particle
from barneshut import Node


c = Constants()

root = Node(0, 0, c.bound)

fig, ax = plt.pyplot.subplots(figsize=(6, 6))

ax.set_xlim(0, c.bound)
ax.set_ylim(0, c.bound)
ax.set_aspect('equal')

particle = Particle(1, Vector(550, 550))
particle1 = Particle(1, Vector(270,200))
particle2 = Particle(1, Vector(10, 100))
particle3 = Particle(1, Vector(550, 700))

root.addParticle(particle)
root.addParticle(particle1)
root.addParticle(particle2)
root.addParticle(particle3)


for i in range(len(root.children)):
    print(i)
    print(root.children[i])

    if (len(root.children[i].children) > 0):
        for j in range(len(root.children)):
            print("{}, {}".format(i, j))
            print(root.children[i].children[j])

root.drawTree(ax)

plt.pyplot.show()




