#Create an event driven Zoo-Keeping system

import random

security_channel = []
zoo_keeper_channel = []
vet_channel = []
guard_channel = []
manager_channel = []


class Sensor:
    def __init__(self, sensor_type, sensor_id):
        self.sensor_type = sensor_type
        self.sensor_id = sensor_id


class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

class Employee:
    def __init__(self, name, emp_id, role):
        self.name = name
        self.emp_id = emp_id
        self.role = role


s1 = Sensor("Humidity", "01")
s2 = Sensor("Temperature", "02")
emp1 = Employee("John", "001", "Guard")
emp2 = Employee("James", "002", "Zoo-Keeper")
emp3 = Employee("Jim", "003", "Cleaner") 

events = [["motion detected", {"location": "Cage ABC"}], ["dirty cage", {"location": "Cage A58"}], ["temperature_rise", {"location": "Cage ABC", "temp": "40"}]]

event = random.choice(events)
print(event)

def run_event():
    if event == "motion detected":
        print(f"{emp1.name} is checking the cage")
    elif event == "dirty cage":
        print(f"{emp1.name} is cleaning the cage")
    elif event == "temperature_rise":
        print(f"{emp1.name} is checking the cage temperature")

run_event()

    

