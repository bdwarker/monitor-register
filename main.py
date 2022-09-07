#Importing libraries for later
import json
from datetime import datetime
from datetime import date
from re import sub
import time
import os

f = open('assets/teachersData.json') # Accessing the database containing teacher's data
teachersData = json.load(f) # Loading the Json file to use it.
crtTime = time.strptime(datetime.now().strftime('%H:%M'), '%H:%M') # Getting current time to compare with the times for the periods to get which period is going on.
while True: # Creating a loop so it keeps running.
    ap = input("Name of the teacher: ") # Temporary Input, will be replaced with a barcode scanner
    
    # Comparing today's date to get which day is today.
    if date.today().weekday() == 0:
        day = "Monday"
    elif date.today().weekday() == 1:
        day = "Tuesday"
    elif date.today().weekday() == 2:
        day = "Monday"
    elif date.today().weekday() == 3:
        day = "Thursday"
    elif date.today().weekday() == 4:
        day = "Friday"
    elif date.today().weekday() == 5:
        day = "Saturday"
    
    # per1 = ("8:50", "9:30")
    # per2 = ("9:50", "10:10")
    # per3 = ("10:10", "10:50")
    # per4 = ("10:50", "11:30")
    # per5 = ("12:00", "12:40")
    # per6 = ("12:40", "13:20")
    # per7 = ("13:20", "14:00")
    # per8 = ("14:00", "14:40")

    # Comparing the time to see which period is going on.
    if crtTime >= time.strptime('8:50', '%H:%M') and crtTime < time.strptime('9:30', '%H:%M'):
        peri = "1st_Period"
    elif crtTime >= time.strptime('9:30', '%H:%M') and crtTime < time.strptime('10:10', '%H:%M'):
        peri = "2nd_Period"
    elif crtTime >= time.strptime('10:10', '%H:%M') and crtTime < time.strptime('10:50', '%H:%M'):
        peri = "3rd_Period"
    elif crtTime >= time.strptime('10:50', '%H:%M') and crtTime < time.strptime('11:30', '%H:%M'):
        peri = "4th_Period"
    elif crtTime >= time.strptime('12:00', '%H:%M') and crtTime < time.strptime('12:40', '%H:%M'):
        peri = "5th_Period"
    elif crtTime >= time.strptime('12:40', '%H:%M') and crtTime < time.strptime('13:20', '%H:%M'):
        peri = "6th_Period"
    elif crtTime >= time.strptime('13:20', '%H:%M') and crtTime < time.strptime('14:00', '%H:%M'):
        peri = "7th_Period"
    elif crtTime >= time.strptime('14:00', '%H:%M') and crtTime < time.strptime('14:40', '%H:%M'):
        peri = "8th_Period"

    # Checking if teachers name is there in the value of the current period going on in the database.
    if ap == teachersData[f"{day}"][f"{peri}"]['name']:
        # Getting information on the teacher.
        name = teachersData[f"{day}"][f"{peri}"]['name'] # Getting teachers name for the output
        arrivalTime = teachersData[f"{day}"][f"{peri}"]["arrival"] # Getting the arrival time in the database for comparision
        departureTime = teachersData[f"{day}"][f"{peri}"]["departure"] # Getting the departure time in the database for comparision
        subject = teachersData[f"{day}"][f"{peri}"]['Subject'] # Getting subject taught by the teacher for the output

        now = datetime.now() # Getting current time to check the arrival time.
        current_time = now.strftime("%H:%M") # Transforming time to Hours and Minutes

        # Checking if the arrival time matches the arrival time in the database to see if it is an arrangement or not.
        if time.strptime(current_time, '%H:%M') >= time.strptime(arrivalTime, '%H:%M') and time.strptime(current_time, '%H:%M') < time.strptime(departureTime, '%H:%M'):
            arrt='False' # Setting the arrangement value to false
        else:
            arrt='True' # Setting the arrangement value to true

    # If the teacher's name is not for the current period, this will be executed and the period will be marked as arrangement.
    elif ap != teachersData[f"{day}"][f"{peri}"]['name']:
        # Getting information on the teacher.
        name = ap
        now = datetime.now() # Getting the current time.
        current_time = now.strftime("%H:%M") # Transforming time to Hours and Minutes
        subject = "NA" # Setting the subject to 'NA' as its an arrangement
        arrt = "True" # Setting the arrangement value to true
        arrivalTime = current_time # Setting the arrival time to current time
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
    
    try: # Trying to make the output file if it doesn't exists
        os.mkdir("assets/output") # Making output folder under assets
        fpi = open(f'assets/output/{today}.txt', 'x') # Opening the file as write-only with out clearing it completely.
        fpi.close() # Closing the file so it saves.
    except: # If any error occurs it passes because the error was caused due to the file already existing.
        pass # Pass
    # Writing data in file
    fp = open(f'assets/output/{today}.txt', 'r') # Opening ouput as read-only
    orgContent = fp.read() # Reading the original content and saving it for later.
    fp.close() # Closing the file so it saves.
    fp2 = open(f'assets/output/{today}.txt', 'r+') # Re-opening the file as read and write
    fp2.write(orgContent + "\n" + str(out)) # Writing the orignal content and the output dictionary created earlier
    fp2.close() # CLosing the file so it saves.

    
    