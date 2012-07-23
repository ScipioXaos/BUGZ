# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     Screen.py is the main component of the BUGZ! rendering
#                       software.  It also handles control input.

from Tkinter import *
import tkFont

# Class Description:    Screen is the rendering component of BUGZ!  It uses the
#                       built-in Tkinter module to do so.
class Screen:
    
    buttons = {}
    game = False
    
    def __init__(self, menu_main, core):
        
        self.core = core
        
        self.root = Tk()
        self.root.geometry('800x600')
        self.root.resizable(width=False, height=False)
        
        # window_main = Frame(root, width = 800, height = 600)
        self.screen = Canvas(self.root, width = 800, height = 600)
        self.screen.focus_force()
        
        load_menu(menu_main)
        
        root.mainloop()
        
    def load_menu(self, menu_):
        self.game = False
        self.screen.delete(ALL)
        
        self.bg = screen.create_image(menu_.get_bg())
        
        for button in menu_.get_buttons():
            button_font = tkFont.Font(family=button[1][2], size=button[1][3])
            new_button_id = screen.create_text(button[0], button[1][0],
                                               button[1][1],
                                               font=button_font, 
                                               fill=button[1][4],
                                               activefill=button[1][5])
            self.screen.tag_bind(new_button_id, "<Button-1>", 
                                 self._send_message_to_core)
            self.buttons[new_button_id] = button[3]
        
    
    def load_game(self, game_):
        self.screen.delete(ALL)
        
        self.bg = screen.create_image(game_)
        self.game = True
        
    def _send_message_to_core(self, event):
        if event.widget in self.buttons:
            self.core.command(self.buttons[event.widget])