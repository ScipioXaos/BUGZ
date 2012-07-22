# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     Location.py is a wrapper class used to pair two integers
#                       together.  These integers represent an X-Y coordinate
#                       pair and a "Location" in a Map instance.

# Class Description:    Location is the wrapper class used to represent an
#                       X-Y coordinate pair in a more efficient manner.
class Location:
    
    def __init__(self, y, x):
        self.y = y
        self.x = x
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_coords(self, y, x):
        self.y = y
        self.x = x
        
    def set_x(self, x):
        self.x = x
        
    def set_y(self, y):
        self.y = y
        