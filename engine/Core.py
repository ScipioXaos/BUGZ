# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     Core.py is the engine "core" that oversees all the 
#                       processing of the game.

from engine.render import Screen
from engine.world import World

class Core:
    
    in_game = False
    in_menu = True
    done = True
    application_running = True
    cmd = None
    
    def __init__(self):
        self.render = Screen(main_menu, self)
    
    def start_game(self):
        
        while application_running:
            in_menu = self.in_menu
            done = self.done
            in_game = self.in_game
            
            if self.cmd != None:
                cmd, self.cmd = self.cmd, None
            if in_menu and done == False:
                if cmd == 'TITLE':
                    self.render.load_menu(main_menu)
                elif cmd == 'PAUSE':
                    self.render.load_menu(pause_menu)
                self.done = True
            if in_game:
                self.world.update_game_state(cmd)
                image = _get_game_state()
                self.render.load_game(image)
    
    def command(self, cmd):
        if cmd == 'LOAD_WORLD':
            self.world = World(self.mappack)
            self.in_menu = False
            self.in_game = True
        if cmd == 'QUIT':
            self.application_running = False
            self.in_menu = False
            self.render.root.destroy()
        if cmd == 'CONTINUE':
            self.in_menu = False
            self.in_game = True
        if cmd == 'TITLE':
            self.cmd = cmd
        if cmd == 'PAUSE':
            self.cmd = cmd
        