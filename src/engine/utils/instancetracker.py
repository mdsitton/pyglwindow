class Tracker:
    def __init__(self):
        self.instances = {self.__class__.__name__: self}
    
    def get(self, name):
        if name in self.instances.keys():
            return self.instances[name]
        else:
            return None
    
    def set(self, instance, name = None):
        if name is None:
            name = instance.__class__.__name__
        
        self.instances[name] = instance
    
    def remove(self, name):
        del self.instances[name]
    
    def printall(self):
        print (self.instances)

InstanceTracker = Tracker()