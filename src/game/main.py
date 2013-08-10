from src.engine.bindings.opengl import *
from src.engine.window import Window
from src.engine.context import Context
from src.engine.utils.file import get_path

class Main(object):
    ''' Starting class of all game specific code '''
    def __init__(self, width=1280, height=720, fullscreen=False):

        self.width = width
        self.height = height

        self.fullscreen = fullscreen

        self.title = "Hello World!"
        
        self.running = True

        self.path = get_path()

        # FPS counter
        self.fpstimer = Timer()
        self.frames = 0
        self.time = 0
        
        self.events = Events()
        InstanceTracker.set(self.events)
        
        self.window = Window(self.width, self.height, self.fullscreen, self.title, 3.3)
        
        InstanceTracker.set(self.window)
        
        self.events.register_type('on_close')
        self.events.register_type('on_resize')
        self.events.register_type('on_paint')
        
        self.events.add_listener('Main', self.event_listener)
        
        self.init_ogl()

        self.window.set_visibility(True)
        
        self.run()
    
    def init_ogl(self):
                             
        glVersionMajor = c_int(-1)
        glVersionMinor = c_int(-1)
        glGetIntegerv(GL_MAJOR_VERSION, pointer(glVersionMajor))
        glGetIntegerv(GL_MINOR_VERSION, pointer(glVersionMinor))

        # Once we create a logging system move this to 
        
    def event_listener(self, event, data):
        if event == 'on_resize':
            width = data['width']
            height = data['height']
            self.resize(width, height)
        elif event == 'on_close':
            self.exit()
        #elif event == 'on_paint':
            #print ('painting now :D')
    
    def run(self):
        while self.running:
            self.events.process()
            
            self.update()
            self.render()

    def update(self):
        ''' Put everything other than rendering here'''
        pass

    def resize(self, width, height):
        ''' Called when the context resizes '''
        glViewport(0, 0, width, height)
        glClearColor(1.0, 1.0, 1.0, 1.0)
    
    def render(self):
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        self.window.flip()

        self.tickTime = self.fpstimer.tick()

        # FPS counter
        self.time += self.tickTime
        self.frames += 1
        if self.time >= 2000:
            print ('FPS: {0}'.format(self.frames / 2))
            self.frames = 0
            self.time = 0

    def exit(self):
        ''' Cleanup code, called right before the context is destroyed '''
        self.running = False

if __name__ == "__main__":
    Main()
