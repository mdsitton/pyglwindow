import src.library.x11 as x11

from src.engine.utils.file import resolve_path
#from src.engine.display import Display

# Constants
FULLSCREEN = 1
WINDOWED = 2

class Window(object):
    def __init__(self, width, height, fullscreen, title):
        
        self.title = title
        self.width = width
        self.height = height

        self._contextClass = None
        self._context = None

        self._events = None
        self._windowMode = None

        self._window = None

        self._disp = x11.XOpenDisplay(x11.ct.cast(0, x11.ct.c_char_p))
        self._dfscr = x11.XDefaultScreen(self._disp)

        self._blkpx = x11.XBlackPixel(self._disp, self._dfscr)


        self._dfrwin = x11.XDefaultRootWindow(self._disp)

        #self.display = Display()
        #self.monitorInfo, self.monitorCount = self.display.get_monitors()

        self.dataPath = resolve_path('data')

        self._window = x11.XCreateSimpleWindow(self._disp, self._dfrwin, 0, 0, self.width, self.height, 0, self._blkpx, self._blkpx)
        x11.XCreateGC(self._disp, self._window, 0, x11.ct.cast(0, x11.ct.POINTER(x11.XGCValues)))

    def delete(self):
        pass

    def _size_listener(self, event, data):
        self.width = data['width']
        self.height = data['height']

    def _setup_events(self):
        self._events.add_listener('window', self._size_listener, exclusive='on_resize')
        self._events.append('on_resize', {'width': self.width, 'height': self.height})

    @property
    def events(self):
        return self._events
    @events.setter
    def events(self, value):
        self._events = value
        self._events.window = self
        self._setup_events()

    @property
    def context(self):
        self._create()
        return self._context
    @context.setter
    def context(self, value):
        self._context = value

    @property
    def visibility(self):
        return self._visibility
    @visibility.setter
    def visibility(self, value):
        self._visibility = value

        if self._visibility:
            x11.XMapWindow(self._disp, self._window)
        if not self._visibility:
            x11.XUnmapWindow(self._disp, self._window)

    
    