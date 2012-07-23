# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     MapParser.py contains the processing code used to take
#                       a <LevelName>.map file and turn it into a Map instance.

from PIL import Image, ImageTk
from engine.entities import Entity, Character_Entity
import Map
import Location

# Class Description:    Converts .map files representing a level of BUGZ! into
#                       information that the Core can process and Render.
class MapParser:
    
    @staticmethod
    def create_map(mapfile):
        map_data = _get_map_data(mapfile)
        entity_set = _create_entity_set(map_data['ENTITIES'])
        tileset = _create_tileset(map_data['TILES'], entity_set)
        map, spawn = _build_map(map_data['MAP'], tileset)
        return map_data['NAME'], map, spawn
        
    @staticmethod
    def _get_map_data(mapfile):
        map_data = {
                    'ENTITIES': [],
                    'TILES': [],
                    'MAP': []
                    }
        mapfile = open(mapfile, 'r')
        read_data = False
        data_type = None
        for line in mapfile:
            line_broken = _break_line(line, ':')
            if line_broken[0] == 'NAME':
                map_data['NAME'] = line[1]
            elif line_broken[0] == 'ENTITIES' and line_broken[1] == 'START':
                read_data = True
                data_type = 'ENTITIES'
            elif line_broken[0] == 'TILES' and line_broken[1] == 'START':
                read_data = True
                data_type = 'TILES'
            elif line_broken[0] == 'MAP' and line_broken[1] == 'START':
                read_data = True
                data_type = 'MAP'
            elif line_broken[1] == 'END':
                read_data = False
                data_type = None
            elif read_data:
                if data_type == 'ENTITIES':
                    map_data['ENTITIES'].append(line)
                elif data_type == 'TILES':
                    map_data['TILES'].append(line)
                elif data_type == 'MAP':
                    map_data['MAP'].append(line)
        return map_data
    
    @staticmethod
    def _break_line(line, token):
        segments = []
        cur_segment = ''
        for chr_ in line:
            if chr_ == token:
                segments.append(cur_segment)
                cur_segment = ''
            else:
                cur_segment += chr_
        return segments
    
    @staticmethod
    def _create_entity_set(entity_data):
        entity_set = {}
        for entity in entity_data:
            new_ent = None
            entity = _break_line(entity, ':')
            attributes = _break_line(entity[1], ';')
            if attributes[0] == 'Entity':
                image = Image.open(_break_line(attributes[1], '=')[1])
                new_ent = Entity(image)
            else: # attributes[0] == 'Character_Entity':
                ent_stats = Character_Entity.Statistics()
                stats = (_break_line(attributes[1], '=')[1])
                for stat in stats:
                    stat = _break_line(stat, '=')
                    ent_stats[stat[0]] = stat[1]
                image = Image.open(_break_line(attributes[2], '=')[1])
                ai = _break_line(attributes[3], '=')[1]
                new_ent = Character_Entity(image, ai, stats)
            entity_set[entity[0]] = new_ent
        return entity_set
    
    @staticmethod
    def _create_tileset(tile_data, entity_set):
        tileset = {}
        
        for tile in tile_data:
            tile = _break_line(tile, ':')
            attributes = _break_line(tile[1], ';')
            new_tile = None
            image = None
            occupant = None
            passable = True
            for attribute in attributes:
                attribute = _break_line(attribute, '=')
                if attribute[0] == 'image':
                    image = Image.open(attribute[1])
                elif attribute[0] == 'occupant':
                    occupant == attribute[1]
                else: # attribute[0] == 'passable':
                    passable = attribute[1]
            new_tile = Map.Tile(image, passable, occupant)
            tileset[tile[0]] = new_tile
    
    @staticmethod
    def _build_map(map_format, tileset):
        map = []
        spawn = False
        for row in map_format:
            map.append([])
            row = _break_line(row, ':')
            tile_definitions = _break_line(row[1], ';')
            for definition in tile_definitions:
                if definition[0] == '[':
                    definition = _expand_defintion(tileset[defintion])
                    for ex_def in definition:
                        tile = tileset[ex_def]
                        if tile.get_occupant() == 'SPAWN':
                            spawn = Location(row[0], len(map[row[0]]))
                            tile.remove_occupant(False)
                        map[row[0]].append(tile)
                else:
                    tile = tileset[definition]
                    if tile.get_occupant() == 'SPAWN':
                        spawn = Location(row[0], len(map[row[0]]))
                        tile.remove_occupant(False)
                    map[row[0]].append(tile)
        return map, spawn
    
    @staticmethod
    def _expand_definition(definition):
        end = defintion.find(']')
        sequence_unrefined = definition[1:end]
        exp = definition[end:]
        sequence = _break_line(sequence_unrefined, '|')
        if exp[0] == '*':
            sequence *= int(exp[1:])
        return sequence
        