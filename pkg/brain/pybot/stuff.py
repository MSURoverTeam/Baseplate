import rospy

from brain.msg import Event
from brain.srv import GetEvent, GetEventResponse


EVENTS = [
    "New Year",
    "Wedding",
    "Labor Day",
    "Bought a new dog",
    "DnD evening"
]


def get_event(req):
    if req.index >= len(EVENTS):
        event = "No idea!"
    else:
        event = EVENTS[req.index]
    return GetEventResponse(Event(event))


def create_service():
    return rospy.Service('get_event', GetEvent, get_event)
