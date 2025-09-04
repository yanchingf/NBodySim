
# she quad on my tree until i subdivide
# https://arborjs.org/docs/barnes-hut

from particle import Particle
from vector import Vector

import matplotlib as plt
from matplotlib import pyplot
from matplotlib.patches import Rectangle

class Node:

    def __init__(self, x, y, bound):
        
        # box drawing
        self.x = x
        self.y = y
        self.bound = bound

        self.isleaf = True

        self.num_bodies = 0
        self.total_mass = 0

        # center of mass coords
        self.com_pos = Vector(0,0)

        self.particle = None

        self.children = []


    def __str__(self):
       
       return (
          "Coordinates: ({}, {}) \n".format(self.x, self.y) +
          "Current Particle: {} \n".format(self.particle) +
          "Bound: {} \n".format(self.bound) + 
          "Children: {} \n".format(self.children)
       )

    
    # NW [0] SW [1] SE [2] NE [3]

    def split(self):
        
        child_bound = self.bound / 2

        self.children = [
            Node(self.x, self.y, child_bound),
            Node(self.x + child_bound, self.y, child_bound),
            Node(self.x, self.y + child_bound, child_bound),
            Node(self.x + child_bound, self.y + child_bound, child_bound)
        ]


    # call from parent
    def placeParticle(self, particle):
        
      child_bound = self.bound / 2

      x = particle.pos.x
      y = particle.pos.y

      if x <= self.x + child_bound and y <= self.y + child_bound:
        return 0
      if x > self.x + child_bound and y <= self.y + child_bound:
        return 1
      if x > self.x + child_bound and y > self.y + child_bound:
        return 2
      else:
        return 3


    def addParticle(self, p):
        
        if (self.isleaf == True):

            # empty / external
            if (self.particle == None):
           
              self.particle = p
              self.com_pos.add(p.pos)
              self.total_mass += p.mass
              self.num_bodies += 1


            # not empty —> split tree
            else:
                
                self.isleaf = False
                
                particle_1 = self.particle
                particle_2 = p
                
                working_node = self
                
                placement_1 = working_node.placeParticle(particle_1)
                placement_2 = working_node.placeParticle(particle_2)

                # recursively split if same quadrant
                while (placement_1 == placement_2):
                   
                  working_node.split()
                   
                  working_node = working_node.children[placement_1] 
                  print(working_node)

                  placement_1 = working_node.placeParticle(particle_1)
                  placement_2 = working_node.placeParticle(particle_2)

                  working_node.com_pos.add(particle_1.pos.add(particle_2.pos))

                  working_node.total_mass += (particle_1.mass + particle_2.mass)
                  working_node.num_bodies += 2

                
                # placement
                working_node.split()

                working_node.children[placement_1].particle = particle_1
                working_node.children[placement_2].particle = particle_2

                working_node.children[placement_1].com_pos.add(particle_1.pos)
                working_node.children[placement_2].com_pos.add(particle_2.pos)

                working_node.children[placement_1].total_mass += particle_1.mass
                working_node.children[placement_2].total_mass += particle_2.mass

                working_node.children[placement_1].num_bodies += 1
                working_node.children[placement_2].num_bodies += 1

                # clear top-level node
                self.particle = None

        # not external —> call place func recursively
        else:
           
           self.particle = p
           self.com_pos.add(p.pos)
           self.total_mass += p.mass
           self.num_bodies += 1

           placement = self.placeParticle(p)
           self.children[placement].addParticle(p)


    # draw box
    def drawNode(self, ax):

       rec = Rectangle((self.x, self.y), self.bound, self.bound,
             edgecolor = 'blue',
             fill=False,
             lw=0.5)
       
       ax.add_patch(rec)
       

    # full search and draw, call at head node
    def drawTree(self, ax):
       
       self.drawNode(ax)

       if (self.particle != None):
             ax.plot(self.particle.pos.x, self.particle.pos.y,
                     color = "black", marker = "o", markersize=1)
       
       if (len(self.children) == 0):
          return
       
       else:
          # recurse
          for child in self.children:
             child.drawTree(ax)

