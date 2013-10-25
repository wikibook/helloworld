# Listing-20-5.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Cleaning up the tempGUI code even more
#   by using the command event of 
#   buttons and menu items

from PythonCard import model

class MainWindow(model.Background):

    def on_cmdCtoF_command(self, event):
        Cel = float(self.components.tfCel.text)
        Fahr = Cel * 9.0 / 5 + 32
        print'cel = ', Cel, '  fahr = ', Fahr
        self.components.spinFahr.value = int(Fahr)
        
    def on_cmdFtoC_command(self, event):
        Fahr = self.components.spinFahr.value
        Cel = (Fahr - 32) * 5.0 / 9
        Cel = '%.2f' % Cel
        self.components.tfCel.text = Cel

app = model.Application(MainWindow)
app.MainLoop()
