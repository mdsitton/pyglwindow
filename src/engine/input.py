from src.engine.events import Events
from src.engine.utils.instancetracker import InstanceTracker
import display

class Input(object):
    def __init__(self):
        
        events = InstanceTracker.get('Events')
        
    def register_device(self, type, name)
        events.register_type('')