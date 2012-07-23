# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     Menu.py represents the class that will hold menu
#                       configuration data to be loaded by the render when the
#                       player is accessing a menu.

import MenuParser


class Menu:
    
    bg_image = None
    buttons = {}
    
    def __init__(self, menu_file):
        parse_menu = MenuParser(menu_file)
        self.bg_image = parse_menu.get_bg_image()
        self.buttons = parse_menu.get_buttons()
    
    def get_bg(self):
        return self.bg_image
    
    def get_buttons(self):
        return self.buttons