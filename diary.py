#Importing libraries for later
import json
from datetime import datetime
from datetime import date
import time
import os
import modules.date as md
import modules.teachersData as td
import modules.saveOut as saveOut
f = open('assets/teachersData.json') # Accessing the database containing teacher's data
teachersData = json.load(f) # Loading the Json file to use it.
crtTime = time.strptime(datetime.now().strftime('%H:%M'), '%H:%M') # Getting current time to compare with the times for the periods to get which period is going on.
while True: # Creating a loop so it keeps running.
    ap = input("Name of the teacher: ") # Temporary Input, will be replaced with a barcode scanner
    day = md.checkDay()
    peri = md.checkTime(crtTime = crtTime)
    # Checking if teachers name is there in the value of the current period going on in the database.
    if ap == str(td.getName(day=day, peri=peri)):
        # Getting information on the teacher.
        name = str(td.getName(day=day, peri=peri)) # Getting teachers name for the output
        arrivalTime = str(td.getArrival(day=day, peri=peri)) # Getting the arrival time in the database for comparision
        departureTime = str(td.getDeparture(day=day, peri=peri)) # Getting the departure time in the database for comparision
        subject = str(td.getSubject(day=day, peri=peri)) # Getting subject taught by the teacher for the output

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
    saveOut.saveFile(peri=peri, name=name, subject=subject, arrivalTime=current_time, arrt=arrt)

    
    