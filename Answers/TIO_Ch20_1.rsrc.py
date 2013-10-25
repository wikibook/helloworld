# TIO_Ch20_1.rsrc.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Resource file for NumberGuess Pythoncard program

{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'NumGuess',
          'title':u'Number Guess',
          'size':(400, 300),
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

{'type':'StaticText', 
    'name':'StaticText5', 
    'position':(32, 204), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'text':u'st', 
    },

{'type':'StaticText', 
    'name':'StaticText2', 
    'position':(17, 31), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'text':u"It is a number from 1 to 99.  I'll give you 6 tries.", 
    },

{'type':'StaticText', 
    'name':'StaticText1', 
    'position':(16, 10), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'text':u"AHOY!  I'm the Dread Pirate Roberts, and I have a secret!", 
    },

{'type':'StaticText', 
    'name':'StaticText4', 
    'position':(32, 178), 
    'font':{'style': 'bold', 'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'text':u'StaticText2', 
    },

{'type':'Button', 
    'name':'btnGuess', 
    'position':(26, 139), 
    'label':u'Guess!', 
    },

{'type':'StaticText', 
    'name':'StaticText3', 
    'position':(23, 78), 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 10}, 
    'text':u'Type in your guess, then click the Guess button.', 
    },

{'type':'Spinner', 
    'name':'Spinner1', 
    'position':(24, 107), 
    'max':100, 
    'min':0, 
    'value':0, 
    },

] # end components
} # end background
] # end backgrounds
} }
