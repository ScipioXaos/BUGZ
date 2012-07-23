# BUGZ! - A Python 'Learning' Adventure coded in Python!
# Project Description:  A Python Game to help Udacity CS101 students
#                       understand Python with emphasis on Object-Oriented
#                       Programming.
# File Description:     BUGZ.py is used to launch the game.

import engine.core

try:
    import PIL # Tests to see if Library is present on User system.
    
    game_core = core()
    
except:
    print "PYTHON IMAGING LIBRARY REQUIRED TO RUN BUGZ!"
    print "DOWNLOAD IT HERE AT: "
    print "http://www.pythonware.com/products/pil/"
    print ""
    print "ENDING PROGRAM"