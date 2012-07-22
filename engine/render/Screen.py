# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     Screen.py is the main component of the BUGZ! rendering
#                       software.  It also handles control input.

from Tkinter import *

# Class Description:    Screen is the rendering component of BUGZ!  It uses the
#                       built-in Tkinter module to do so.
class Screen:
    
    def __init__(self, menu_main, core):
        
        self.core = core
        
        root = Tk()
        
        root.resizable(width=False, height=False)
        
        window_main = Frame(root, width = 800, height = 600)
        self.screen = Canvas(window_main, width = 800, height = 600)
        
        load_menu(menu_main)
        
        mainloop()
        
    def load_menu(self, menu_):
        pass