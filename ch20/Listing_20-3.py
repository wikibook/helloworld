# Listing_20-3.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Adding menu event handlers

from PythonCard import model

class MainWindow(model.Background):
            
    def on_btnCtoF_mouseClick(self, event):
        cel = float(self.components.tfCel.text)
        fahr = cel * 9.0 / 5 + 32
        print'cel = ', cel, '  fahr = ', fahr
        self.components.spinFahr.value = int(Fahr)
        
    def on_btnFtoC_mouseClick(self, event):
        fahr = self.components.spinFahr.value
        cel = (fahr - 32) * 5.0 / 9
        cel = '%.2f' % cel
        self.components.tfCel.text = cel

    def on_menuConvertCtoF_select(self, event):
        cel = float(self.components.tfCel.text)
        fahr = cel * 9.0 / 5 + 32
        print'cel = ', cel, '  fahr = ', fahr
        self.components.spinFahr.value = int(fahr)

    def on_menuConvertFtoC_select(self, event):
        fahr = self.components.spinFahr.value
        cel = (fahr - 32) * 5.0 / 9
        cel = '%.2f' % cel
        self.components.tfCel.text = cel

app = model.Application(MainWindow)
app.MainLoop()