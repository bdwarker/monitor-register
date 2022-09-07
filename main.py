import json
from datetime import datetime
from datetime import date
from re import sub
import time
import os
f = open('assets/teachersData.json')
crtTime = time.strptime(datetime.now().strftime('%H:%M'), '%H:%M')
teachersData = json.load(f)
while True:
    ap = input("Name of the teacher: ")
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

    if ap == teachersData[f"{day}"][f"{peri}"]['name']:
        name = teachersData[f"{day}"][f"{peri}"]['name']
        arrivalTime = teachersData[f"{day}"][f"{peri}"]["arrival"]
        departureTime = teachersData[f"{day}"][f"{peri}"]["departure"]
        subject = teachersData[f"{day}"][f"{peri}"]['Subject']
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if time.strptime(current_time, '%H:%M') >= time.strptime(arrivalTime, '%H:%M') and time.strptime(current_time, '%H:%M') < time.strptime(departureTime, '%H:%M'):
            arrt='False'
        else:
            arrt='True'
    elif ap != teachersData[f"{day}"][f"{peri}"]['name']:
        name = ap
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        subject = "NA"
        arrt = "True"
        arrivalTime = current_time
    today = date.today()
    out = {
        f"{peri}": {
            "name": str(name),
            "subject": str(subject),
            "arrivalTime": str(arrivalTime),
            "Arrangement": str(arrt)
        }
    }
    
    try:
        os.mkdir("assets/output")
        fpi = open(f'assets/output/{today}.txt', 'x')
        fpi.close()
    except:
        pass
    fp = open(f'assets/output/{today}.txt', 'r')
    orgContent = fp.read()
    fp.close()
    fp2 = open(f'assets/output/{today}.txt', 'r+')
    fp2.write(" ")
    fp2.write(orgContent + "\n" + str(out))
    fp2.close()

    
    