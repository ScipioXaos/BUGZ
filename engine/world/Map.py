# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     Map.py is used to represent "maps" or levels that exist
#                       in the game.  Maps are held inside a World object.

import MapParser

# Class Description:    Map is the object used to represent a level in BUGZ!
#                       Composed of Tile objects inside a two-dimensional array.
class Map:
    
    def __init__(self, mapfile):        
        self.name, self.map, self.spawn = MapParser.create_map(mapfile)
        
    def get_map_name(self):
        return self.name
        
    def get_occupant(self, loc):
        self.map[loc.get_y][loc.get_x].get_occupant()
    
    def is_occupied(self, loc):
        return self.map[loc.get_y()][loc.get_x()].get_occupant() is not None

# Class Description:    Tile is the reperesntation of a single grid in a Map.
#                       Tile instances are stored in a Map instance and hold all
#                       the data about the entities that occupy said Tile and
#                       the graphical content unique to the Tile as well as
#                       important map data.
class Tile:
    
    occupant = None
    
    def __init__(self, image, passable, occupant):
        self.image = image
        self.passable = passable
        self.occupant = occupant
        
    def get_occupant(self):
        return self.occupant
    
    def set_occupant(self, entity):
        if self.passable:
            self.occupant = entity
        else:
            print "PROGRAM ERROR: TILE NOT PASSABLE"
        
    def remove_occupant(self, get):
        if get:
            temp = occupant
            self.occupant = None
            return temp
        self.occupant = None
        
    def set_passable(self, bool_):
        self.passable = bool_
        
    def is_passable(self):
        return self.passable