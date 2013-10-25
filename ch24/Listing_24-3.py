# Listing_24-3.py
# Copyright Warren Sande, 2009
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version 61  ----------------------------

# Saving time to a pickle file

import datetime, pickle                                                    
import os                                                                  

first_time = True
if os.path.isfile("last_run.pkl"):                                         
    pickle_file = open("last_run.pkl", 'r')                                
    last_time = pickle.load(pickle_file)                                   
    pickle_file.close()
    print "The last time this program was run was ", last_time
    first_time = False
    
pickle_file = open("last_run.pkl", 'w')                                    
pickle.dump(datetime.datetime.now(), pickle_file)                          
pickle_file.close()
if first_time:
    print "Created new pickle file."
