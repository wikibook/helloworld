# colormixer.rsrc.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Resource file for colormixer.py

{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Color Mixer',
          'size':(400, 396),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'btnChooseColor', 
    'position':(98, 288), 
    'size':(197, -1), 
    'label':u'Advanced Color Picker', 
    },

{'type':'StaticText', 
    'name':'stBlue', 
    'position':(334, 248), 
    'text':u'0', 
    },

{'type':'StaticText', 
    'name':'stGreen', 
    'position':(334, 208), 
    'text':u'0', 
    },

{'type':'StaticText', 
    'name':'stRed', 
    'position':(334, 168), 
    'text':u'0', 
    },

{'type':'StaticText', 
    'name':'StaticText3', 
    'position':(20, 248), 
    'text':u'Blue', 
    },

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(20, 208), 
    'alignment':u'right', 
    'text':u'Green', 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(20, 168), 
    'alignment':u'right', 
    'text':u'Red', 
    },

{'type':'Slider', 
    'name':'sliderBlue', 
    'position':(60, 248), 
    'size':(265, -1), 
    'labels':False, 
    'layout':u'horizontal', 
    'max':255, 
    'min':0, 
    'tickFrequency':0, 
    'ticks':False, 
    'value':0, 
    },

{'type':'Slider', 
    'name':'sliderGreen', 
    'position':(60, 208), 
    'size':(265, -1), 
    'labels':False, 
    'layout':'horizontal', 
    'max':255, 
    'min':0, 
    'tickFrequency':0, 
    'ticks':False, 
    'value':0, 
    },

{'type':'Slider', 
    'name':'sliderRed', 
    'position':(60, 168), 
    'size':(265, -1), 
    'labels':False, 
    'layout':u'horizontal', 
    'max':255, 
    'min':0, 
    'tickFrequency':0, 
    'ticks':False, 
    'value':0, 
    },

{'type':'BitmapCanvas', 
    'name':'colorDisplay', 
    'position':(14, 14), 
    'size':(340, 140), 
    'backgroundColor':(255, 255, 255, 255), 
    },

] # end components
} # end background
] # end backgrounds
} }