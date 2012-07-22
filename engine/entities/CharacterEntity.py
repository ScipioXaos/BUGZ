# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     CharacterEntity.py holds the "character" subclass
#                       implementation of Entity located in Entity.py.  It also
#                       contains a "meta data" class used to specify the 
#                       characteristics of CharacterEntity instantiations.

import Entity

# Class Description:    CharacterEntity is a subclass of Entity and is used to
#                       create characters to populate the map.
class CharacterEntity(Entity):
    
    def __init__(self, image, ai, stats):
        Entity.__init__(image)
        self.ai = ai
        set_Statistics(stats)
        
    def set_statistics(self, stats):
        self.stats = stats

# Class Description:    Statistics is a helper class that is used to define the
#                       attributes of different characters in BUGZ! through the
#                       use of a Dictionary.
class Statistics:
    
    stats = {
        'max_health': 0,
        'health': 0,
        'base_attack': 0,
        'base_defense': 0
    }
    
    def __init__(self, max_health, health, base_attack, base_defense):
        self.stats['max_health'] = max_health
        self.stats['health'] = health
        self.stats['base_attack'] = base_attack
        self.stats['base_defense'] = base_defense
        
    def __getitem__(self, stat):
        if stat in self.stats:
            return self.stats[stat]
        return None
    
    def __setitem__(self, stat, value):
        self.stats[stat] = value
        