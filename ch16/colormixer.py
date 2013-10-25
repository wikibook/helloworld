# colormixer.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------


# A PythonCard program to mix red, green and blue 
# and see the resulting color.

from PythonCard import model, dialog

class MyBackground(model.Background):
    def updateColor(self):
        comp = self.components
        canvas = comp.colorDisplay
        canvas.clear()
        canvas.backgroundColor = [comp.sliderRed.value, comp.sliderGreen.value, comp.sliderBlue.value]
        canvas.refresh()
        comp.stRed.text = str(comp.sliderRed.value)
        comp.stGreen.text = str(comp.sliderGreen.value)
        comp.stBlue.text = str(comp.sliderBlue.value)
    
    def on_initialize(self, event):
        self.components.colorDisplay.backgroundColor = [0, 0, 0]
        self.updateColor()

    def on_select(self, event):
        comp = self.components
        canvas = comp.colorDisplay
        name = event.target.name
        if name.startswith('slider'): 
            labelName = 'st' + name[6:]
            comp[labelName].text = str(event.target.value)
        self.updateColor()
    
    def on_btnChooseColor_mouseClick(self, event):
        comp = self.components
        result = dialog.colorDialog(self, color=comp.colorDisplay.backgroundColor)
        if result.accepted:
            my_color = result.color
            comp.colorDisplay.backgroundColor = my_color
            comp.sliderRed.value = my_color[0]
            comp.sliderGreen.value = my_color[1]
            comp.sliderBlue.value = my_color[2]
            self.updateColor()


app = model.Application(MyBackground)
app.MainLoop()