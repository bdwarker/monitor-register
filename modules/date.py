from datetime import datetime
from datetime import date
from glob import glob
import time
def checkDay():
    # Comparing today's date to get which day is today.
    if date.today().weekday() == 0:
        day = "Monday"
    elif date.today().weekday() == 1:
        day = "Tuesday"
    elif date.today().weekday() == 2:
        day = "Wednesday"
    elif date.today().weekday() == 3:
        day = "Thursday"
    elif date.today().weekday() == 4:
        day = "Friday"
    elif date.today().weekday() == 5:
        day = "Saturday"
    return day

def checkTime(crtTime):
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
    elif crtTime >= time.strptime('13:20', '%H:%M') and crtTime < time.strptime('22:00', '%H:%M'):
        peri = "7th_Period"
    elif crtTime >= time.strptime('14:00', '%H:%M') and crtTime < time.strptime('14:40', '%H:%M'):
        peri = "8th_Period"
    return peri