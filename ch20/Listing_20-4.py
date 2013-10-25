# Listing_20-4.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Cleaning up the tempGUI code

from PythonCard import model

def CtoF(self):
    cel = float(self.components.tfCel.text)
    fahr = cel * 9.0 / 5 + 32
    print'cel = ', cel, '  fahr = ', fahr
    self.components.spinFahr.value = int(fahr)

def FtoC(self):
    fahr = self.components.spinFahr.value
    cel = (fahr - 32) * 5.0 / 9
    cel = '%.2f' % cel
    self.components.tfCel.text = cel

class MainWindow(model.Background):

    def on_btnCtoF_mouseClick(self, event):
        CtoF(self)
        
    def on_btnFtoC_mouseClick(self, event):
        FtoC(self)

    def on_menuConvertCtoF_select(self, event):
        CtoF(self)

    def on_menuConvertFtoC_select(self, event):
        FtoC(self)

app = model.Application(MainWindow)
app.MainLoop()