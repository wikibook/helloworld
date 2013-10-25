# Listing_20-1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# an event handler for the Hello button

from PythonCard import model

class MainWindow(model.Background):
    
    def on_helloButton_mouseClick(self, event):
        old_position = self.components.helloButton.position 
        old_x = old_position[0]
        old_y = old_position[1]
        new_x = old_x + 20
        new_y = old_y + 10
        new_position = [new_x, new_y]
        self.components.helloButton.position = new_position

app = model.Application(MainWindow)
app.MainLoop()