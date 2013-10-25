# Listing_20-2.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Complete Temperature Conversion Program

from PythonCard import model

class MainWindow(model.Background):

    def on_btnCtoF_mouseClick(self, event):
        cel = float(self.components.tfCel.text)
        fahr = cel * 9.0 / 5 + 32
        self.components.spinFahr.value = int(fahr)
        
    def on_btnFtoC_mouseClick(self, event):
        fahr = self.components.spinFahr.value
        cel = (fahr - 32) * 5.0 / 9
        self.components.tfCel.text = str(cel)

app = model.Application(MainWindow)
app.MainLoop()