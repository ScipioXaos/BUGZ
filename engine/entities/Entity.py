# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     Entity.py contains the most abstract form of entity
#                       objects and it also contains entity constants.

# Class Description:    Entity is the most abstract form of entities in BUGZ!
class Entity:
    def __init__(self, image):
        self.image = image
    
    def occupy(self, loc, lvl):
        lvl[loc.get_y][loc.get_x].set_occupant(self)
        self.location = loc

    def remove(self):
        lvl[self.location.get_y][self.location.get_x].remove_occupant(False)
        
    def get_image(self):
        return self.image

# Class Description:    EntityConstants is used to hold constant values that
#                       other classes use to determine the relationship between
#                       entities.
class EntityConstants:
    
    PASSIVE = 0
    NEUTRAL = 1
    HOSTILE = 2
    
    PLAYER = 3
    
    DEAD = -1