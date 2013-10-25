# TIO_CH20-1.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Number guess program using PythonCard

from PythonCard import model
import random
guess = 0
secret = random.randint(1, 100)
done = False
tries = 6

class NumGuess(model.Background):

    def on_initialize(self, event):
        self.guess = self.components.Spinner1.value
        self.components.StaticText4.text = ""
        self.components.StaticText5.text = "You have " + str(tries) + " left."

    def on_btnGuess_mouseClick(self, event):
        global done, guess, tries
        if not done:
            if tries > 1:
                if guess != secret:
                    guess = self.components.Spinner1.value       # get the player's guess
                    if guess < secret:
                        self.components.StaticText4.text = "Too low, ye scurvy dog!"
                    elif guess > secret:
                        self.components.StaticText4.text = "Too high, landlubber!"
                    tries = tries - 1                         # used up one try    
                    self.components.StaticText5.text = "You have " + str(tries) + " left."
                
                elif guess == secret:
                    self.components.StaticText4.text = "Avast! Ye got it!  Found my secret, ye did!"
                    self.components.StaticText5.text = ""
                    done = True
            else:
                self.components.StaticText4.text ="No more guesses!  Better luck next time, matey!"
                self.components.StaticText5.text =  "The secret number was " + str(secret)
                done = True
        
app = model.Application(NumGuess)
app.MainLoop()
    