from datetime import datetime

events = []

def log_event(event_type):

    event = {
        "event": event_type,
        "timestamp": str(datetime.now())
    }

    events.append(event)

    return event

def get_events():

    return events