class Event:
    def __init__(self, name, payload):
        self.name = name
        self.payload = payload

def create_event(name, payload):
    return Event(name, payload)

def handle_event(name):
    print(f"{name} is being handled")

handle_event("animal escape")