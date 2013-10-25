# tempgui.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Pythoncard temperature conversion program

from PythonCard import model

class MainWindow(model.Background):

    def on_cmdCtoF_command(self, event):
        cel = float(self.components.tfCel.text)
        fahr = cel * 9.0 / 5 + 32
        self.components.spinFahr.value = int(fahr)
        
    def on_cmdFtoC_command(self, event):
        fahr = self.components.spinFahr.value
        cel = (fahr - 32) * 5.0 / 9
        cel = '%.2f' % cel
        self.components.tfCel.text = cel

app = model.Application(MainWindow)
app.MainLoop()