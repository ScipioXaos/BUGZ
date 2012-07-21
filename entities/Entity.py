# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     Entity.py contains the most abstract form of entity
#                       objects and it also contains entity constants.

# Class Description:    Entity is the most abstract form of entities in BUGZ!
class Entity:
    def __init__(self, loc, image):
        self.x = loc.get_x()
        self.y = loc.get_y()
        self.image = image
    
    def occupy(self, loc, lvl):
        map.lvl[loc.get_x][loc.get_y].set_occupant(self)

    def remove(self):
        world.map[self.x][self.y].remove_occupant(False)
        
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