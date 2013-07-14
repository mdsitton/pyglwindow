from collections import deque

from src.engine.platformevents import PlatformEvents
from src.engine.utils.instancetracker import InstanceTracker

class Events(object):
    ''' Recieves and dispatches events to all '''
    
    def __init__(self):
        self.listeners = {}
        self.eventTypes = []
        
        self.events = deque()
        
        self.platformEvents = PlatformEvents(self)
        InstanceTracker.set(self.platformEvents)
    
    def add_listener(self, name, function, exclusive=None, filter=None):
        if not name in self.listeners.keys():
            self.listeners[name] = {'function': function, 'exclusive': exclusive, 'filter': filter}
            
    def get_listener(self, name):
        ''' Attempts to find a listener which matches the name provided '''
        if name in self.listeners.keys():
            return self.listeners[name]['function']
        else:
            return None
            
    def append(self, event, data):
        self.events.append({'event': event, 'data': data})
        
    def remove_listener(self, name):
        if listener in self.listeners.values():
            del self.listeners[name]
    
    def broadcast(self, name, data):
        for listener in self.listeners.values():
            filter = listener['filter']
            if filter:
                if name in filter:
                    continue
                    
            exclusive = listener['exclusive']
            if exclusive:
                if not name in exclusive:
                    continue
            
            listener['function'](name, data)
    
    def register_type(self, name):
        self.eventTypes.append(name)
    
    def dispatch(self, name, event, data):
        if name in self.listeners.keys():
            self.listeners[name]['function'](event, *data)
        else:
            print ('This event cannot be dispatched')
    
    def process(self):
        self.platformEvents.process()
        
        while len(self.events) > 0:
            
            event = self.events.popleft()
            
            eventName = event['event']
            eventData = event['data']
            
            if eventName in self.eventTypes:
                self.broadcast(eventName, eventData)
        