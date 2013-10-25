import time, datetime, random                                                       
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------


messages = [
    "Of all the trees we could've hit, we had to get one that hits back.",
    "If he doesn't stop trying to save your life he's going to kill you.",
    "It is our choices that show what we truly are, far more than our abilities.",
    "I am a wizard, not a baboon brandishing a stick.",
    "Greatness inspires envy, envy engenders spite, spite spawns lies.",
    "In dreams, we enter a world that's entirely our own.",
    "It is my belief that the truth is generally preferable to lies.",
    "Dawn seemed to follow midnight with indecent haste."
    ]
# Listing_24-2.py
# Typing speed test

print "Typing speed test.  Type the following message.  I will time you."           
time.sleep(2)                                                                       
print "\nReady..."                                                                  
time.sleep(1)                                                                       
print "\nSet..."                                                                    
time.sleep(1)                                                                       
print "\nGo:"                                                                       
message = random.choice(messages)                                                   
print "\n " + message
start_time = datetime.datetime.now()                                                
typing = raw_input('>')
end_time = datetime.datetime.now()                                                  
difference = end_time - start_time
typing_time = difference.seconds + difference.microseconds / float(1000000)         
cps = len(message) / typing_time
wpm = cps * 60 / 5.0                                                                
print "\nYou typed %i characters in %.1f seconds." % (len(message), typing_time)    
print "That's %.2f characters per second, or %.1f words per minute" % (cps, wpm)    
if typing == message:
    print "You didn't make any mistakes."
else:
    print "But, you made at least one mistake."