import json
from datetime import datetime
from datetime import date
import time
f = open('assets/teachersData.json')

teachersData = json.load(f)
ap = input("Name of the teacher: ")
if ap == teachersData["Monday"]["1st_Period"]['name']:
    name = teachersData["Monday"]["1st_Period"]['name']
    arrivalTime = teachersData["Monday"]["1st_Period"]["arrival"]
    departureTime = teachersData["Monday"]["1st_Period"]["departure"]
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if time.strptime(current_time, '%H:%M') >= time.strptime(arrivalTime, '%H:%M') and time.strptime(current_time, '%H:%M') <= time.strptime(departureTime, '%H:%M'):
        arrt='False'
    else:
        arrt='True'
    today = date.today()
    fp = open(f'assets/output/{today}.json', 'w')
    fp.write("""
    {
        "1st_Period": {
            "name" : " """ + f"{str(name)}" + """ ",
            "arrivalTime" : " """ + f"{str(current_time)}" + """ ",
            "Arrangement" : " """ + f"{str(arrt)}" + """ "
        }
    }
    """)

    
    