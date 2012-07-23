# BUGZ! - A Python 'Learning' Adventure coded in Python!
# File Description:     MenuParser.py holds the code required to take a .menu
#                       file and convert it to a menu object.  Unlike MapParser,
#                       MenuParser needs to be instantiated.

from Tkinter import *
import tkFont

class MenuParser:
    
    bg_image = None
    buttons = {}
    
    menu_data = {'BUTTONS': {}}
    
    def __init__(self, menufile):
        self.menu_data = _parse_menu(menufile);
        self.bg_image = PhotoImage(self.menu_data[BG])
        self.buttons = _parse_buttons()
        
    def _parse_menu(self, menufile):
        menufile = open(menufile, 'r')
        menu_data = {}
        read_data = False
        data_type = None
        for line in menufile:
            line = _break_line(line, ':')
            if line[0] == 'RESOLUTION':
                res = _break_line(line[1], ';')
                menu_data[line[0]] = [res[0], res[1]]
            elif line[0] == 'BG':
                menu_data[line[0]] = line[1]
            elif line[0] == 'BUTTONS':
                if line[1] == 'START':
                    read_data = True
                    data_type = 'BUTTONS'
                else:
                    read_data = False
                    data_type = None
            elif read_data == True:
                menu_data[data_type][line[0]] = line[0] + ':' + line[1]
        return menu_data
    
    def _parse_buttons(self):
        buttons = {}
        for button in menu_data['BUTTONS']:
            button = _break_line(button, ':')
            attributes = _break_line(button[1], ';')
            if attributes[0] == 'CENTER':
                attributes[0] = self.menu_data['RESOLUTIONS'][0] / 2
                        #_determine_center(button[0], 
                        #self.menu_data['RESOLUTIONS'][0], attributes[2:4], 'x')
            if attributes[1] == 'CENTER':
                attributes[1] = self.menu_data['RESOLUTIONS'][1] / 2
                        #_determine_center(button[0], 
                        #self.menu_data['RESOLUTIONS'][1], attributes[2:4], 'y')
            buttons[button[0]] = [button[0], attributes[0:-1], attributes[-1]]
        return buttons
    
#    def _determine_center(self, str_, res_value, font_data, dimension):
#        Tk()
#        test_font = tkFont(family=font_data[0], size=font_data[1])
#        coord = 0
#        if dimension == 'x':
#            width = test_font.measure(str_)
#            width = width / 2
#            res_half = res_value / 2
#            coord = res_half - width
#        elif dimension == 'y':
#            height = test_font.metrics('linespace')
#            height = height / 2
#            res_half = res_value / 2
#            coord = res_value - height
#        return coord
    
    def _break_line(self, line, token):
        segments = []
        cur_segment = ''
        for chr_ in line:
            if chr_ == token:
                segments.append(cur_segment)
                cur_segment = ''
            else:
                cur_segment += chr_
        return segments
    
    def get_bg_image(self):
        return self.bg_image
    
    def get_buttons(self):
        return self.buttons