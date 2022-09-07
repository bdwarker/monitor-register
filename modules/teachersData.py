import json

f = open('assets/teachersData.json') # Accessing the database containing teacher's data
teachersData = json.load(f) # Loading the Json file to use it.

def getName(day, peri):
    name = teachersData[f"{day}"][f"{peri}"]['name'] # Getting teachers name for the output
    return name
def getSubject(day, peri):
    subject = teachersData[f"{day}"][f"{peri}"]['Subject'] # Getting subject taught by the teacher for the output
    return subject
def getArrival(day, peri):
    arrivalTime = teachersData[f"{day}"][f"{peri}"]["arrival"] # Getting the arrival time in the database for comparision
    return arrivalTime
def getDeparture(day, peri):
    departureTime = teachersData[f"{day}"][f"{peri}"]["departure"] # Getting the departure time in the database for comparision
    return departureTime