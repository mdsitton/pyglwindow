
from src.engine.utils.file import resolve_path, resolve_file

#from src.engine.context import Context
from src.engine.window import Window
from src.engine.events import Events

DELTA_TIME = 25  # 25 ms time between updates

class Main(object):
    ''' Starting class of all game specific code '''
    def __init__(self, width=1280, height=720, fullscreen=False):

        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        self.title = "Hello World, Lunch Off!"
        
        self.running = True
        
        self.init_engine()
        #self.init_vars()
        #self.init_ogl()

        # Show window
        self.window.visibility = True
        
        self.run()

    def init_engine(self):
        
        # initialize window and its dependants
        self.window = Window(self.width, self.height, self.fullscreen, self.title)
        self.events = Events()
        
        self.context = None

        # transfer instances to window
        self.window.events = self.events
        self.window.context = self.context
        
        # Register events
        self.events.register_type('on_close')
        self.events.register_type('on_resize')
        self.events.register_type('on_run')

        self.events.add_listener('main', self.event_listener)

    def event_listener(self, event, data):
        if event == 'on_resize':
            width = data['width']
            height = data['height']
            self.resize(width, height)
        elif event == 'on_close':
            self.running = False
            print ('test')
        elif event == 'on_run':
            self.do_run()

    def do_run(self):
        self.events.process()

        self.render()
    
    def run(self):
        
        while self.running:
            self.do_run()

        self.exit()


    def update(self):
        ''' Put everything other than rendering here'''
        pass

    def resize(self, width, height):
        ''' Called when the context resizes '''
        print (width, height)

    def render(self):
        ''' Drawing code goes here '''
        pass

    def exit(self):
        ''' Cleanup code, called right before the context is destroyed '''
        #self.context.delete()
        self.window.delete()
