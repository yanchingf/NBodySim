
# she quad on my tree until i subdivide
# https://arborjs.org/docs/barnes-hut

from particle import Particle
from vector import Vector

import matplotlib as plt

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

    
    # NW [0] NE [1] SW [2] SE [3]

    def split(self):
        
        child_bound = self.bound / 2

        self.children = [
            Node(self.x, self.y, child_bound),
            Node(self.x + child_bound, self.y, child_bound),
            Node(self.x, self.y + child_bound, child_bound),
            Node(self.x + child_bound, self.y + child_bound, child_bound)
        ]


    def placeParticle(self, particle):
        
      child_bound = self.bound / 2

      x = particle.pos.x
      y = particle.pos.y

      if x < self.x + child_bound and y < self.y + child_bound:
        return 0
      if x > self.x + child_bound and y < self.y + child_bound:
        return 1
      if x < self.x + child_bound and y > self.y + child_bound:
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

            # not empty / external —> split tree
            else:
                
                self.isleaf = False
                
                particle_1 = self.particle
                particle_2 = p
                
                working_node = self
                
                placement_1 = working_node.placeParticle(particle_1)
                placement_2 = working_node.placeParticle(particle_2)

                # recursively split if same quadrant
                while (placement_1 == placement_2):
                   
                  self.split()
                   
                  working_node = working_node[placement_1]

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
                working_node.children[placement_1].total_mass += particle_2.mass

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
    def drawNode(self):
       coords = (self.x, self.y)
       node = plt.patches.Rectangle(coords, self.bound, self.bound,
                             lineWidth=0.5, edgecolor="blue")
       
       plt.addPatch(node)
       

    # bfs and draw, call at head node
    def drawTree(self):
       
       self.drawNode()
       
       if (len(self.children) == 0):
          return
       else:
          # draw c of m
             

          
          # recurse
          for child in self.children:
             child.drawTree()


    



          
          

       

       



           

        









              











            

                
            

      
 

    


            






        
