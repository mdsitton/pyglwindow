from src.library.opengl import *
from src.engine.utils.file import resolve_path, resolve_file

from src.engine.utils.timehelper import Timer
from src.engine.context import Context
from src.engine.events import Events
from src.engine.window import Window
from src.engine.input import Input

class Main(object):
    ''' Starting class of all game specific code '''
    def __init__(self, width=1280, height=720, fullscreen=False):

        self.width = width
        self.height = height
        self.fullscreen = fullscreen

        self.title = "Hello World, Lunch Off!"

        self.running = True
        
        self.init_engine()
        self.init_vars()
        self.init_ogl()

        # Show window
        self.window.visibility = True
        
        self.run()

    def init_engine(self):
        
        # initialize window and its dependants
        self.window = Window(self.width, self.height, self.fullscreen, self.title)
        self.events = Events()
        self.context = Context(3.3)
        self.input = Input()

        # transfer instances to window
        # Later on down the road rework how this is done.
        # So that we arnt pushing this all into the window code
        # but a class made specifically to push all the instances to where they need to be
        self.window.events = self.events
        self.window.input = self.input
        self.window.context = self.context
        
        # Register events
        self.events.register_type('on_close')
        self.events.register_type('on_resize')
        self.events.register_type('on_run')
        self.events.register_type('on_keydown')
        self.events.register_type('on_keyup')
        self.events.register_type('on_mousedown')
        self.events.register_type('on_mouseup')
        self.events.register_type('on_mousemove')
        
        self.events.add_listener('main', self.event_listener)

    def init_vars(self):

        # render timer
        self.renderTimer = Timer()
        self.frames = 0
        self.renderTime = 0
        self.renderTick = 0.0
        
        self.pressedKeys = []
        
        self.mousePos = [0, 0]
        self.mouseButton = []
    
    def init_ogl(self):

        # Get opengl version number
        glVersionMajor = glGetInteger(GL_MAJOR_VERSION)
        glVersionMinor = glGetInteger(GL_MINOR_VERSION)

        # Once we create a logging system move this to that
        print ("OpenGL Version: {0}.{1}".format(glVersionMinor, glVersionMajor))
       
    def event_listener(self, event, data):
        if event == 'on_resize':
            width = data['width']
            height = data['height']
            self.resize(width, height)
        elif event == 'on_close':
            self.running = False
        elif event == 'on_run':
            self.do_run()
        elif event == 'on_keydown':
            self.pressedKeys.append(data)
        elif event == 'on_keyup':
            self.pressedKeys.remove(data)
        elif event == 'on_mousemove':
            self.mousePos = data
        elif event == 'on_mousedown':
            self.mouseButton.append(data)
        elif event == 'on_mouseup':
            self.mouseButton.remove(data)

    def do_run(self):
        self.events.process()
        self.update()
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
        glViewport(0, 0, width, height)
        glClearColor(1.0, 1.0, 1.0, 1.0)
    
    def render(self):
        ''' Drawing code goes here '''
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)
        self.window.flip()

        # FPS counter
        self.renderTick = self.renderTimer.tick()
        self.renderTime += self.renderTick
        self.frames += 1
        if self.renderTime >= 2000:
            print ('FPS: {0}'.format(self.frames / 2))
            self.frames = 0
            self.renderTime = 0

    def exit(self):
        ''' Cleanup code, called right before the context is destroyed '''
        self.context.delete()
        self.window.delete()
