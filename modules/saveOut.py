from datetime import datetime
from datetime import date
import time
import os
import json
def saveFile(peri, name, subject, arrivalTime, arrt):

    today = date.today() # Getting today's date for the creation of the file.
    # Making a dictionary for cleaner output
    out = {
        f"{peri}": {
            "name": str(name),
            "subject": str(subject),
            "arrivalTime": str(arrivalTime),
            "Arrangement": str(arrt)
        }
    }
    try:
        os.mkdir("assets/output") # Making output folder under assets
    except:
        pass
    try: # Trying to make the output file if it doesn't exists
        fpi = open(f'assets/output/{today}.json', 'x') # Opening the file as write-only with out clearing it completely.
        fpi.close() # Closing the file so it saves.
    except: # If any error occurs it passes because the error was caused due to the file already existing.
        pass # Pass
    # Writing data in file
    fp = open(f'assets/output/{today}.json', 'r') # Opening ouput as read-only
    orgContent = fp.read() # Reading the original content and saving it for later.
    fp.close() # Closing the file so it saves.
    fp2 = open(f'assets/output/{today}.json', 'r+') # Re-opening the file as read and write
    json.dump(out, fp2) # Writing the orignal content and the output dictionary created earlier
    fp2.close() # CLosing the file so it saves.