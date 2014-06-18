import src.library.x11 as x11
from src.engine.events.base import BaseEvents

from src.engine.utils.types import py_str_to_c2

class Events(BaseEvents):
    def __init__(self):
        # set from window once game code gives it the events class
        super(Events, self).__init__()
        self._window = None
        self._disp = None
        self._win = None

    def _init_xevents(self):
        # Setup X11 event masks
        x11.XSelectInput(self._disp, self._win, x11.StructureNotifyMask)

        self.wm_delete_window = x11.XInternAtom(self._disp, py_str_to_c2('WM_DELETE_WINDOW'), 0)
        x11.XSetWMProtocols(self._disp, self._win, x11.ct.pointer(x11.Atom(self.wm_delete_window)), 1)  # for some reason ctypes converts Atom to int

    def process(self):
        e = x11.XEvent()

        while x11.XPending(self._disp):
            x11.XNextEvent(self._disp, x11.ct.byref(e))

            if e.type == x11.ConfigureNotify:
                width = e.xconfigure.width
                height = e.xconfigure.height
                if width != self._window.width and height != self._window.height:
                    self.events.append({'event': 'on_resize', 'data': {'width': width, 'height': height}})
                    self.events.append({'event': 'on_run', 'data': None})
                    
            elif e.type == x11.ClientMessage:
                if e.xclient.data.l[0] == self.wm_delete_window:
                    self.events.append({'event': 'on_close', 'data': None})
            
            self.do_process()

    @property
    def window(self):
        return self._window
    @window.setter
    def window(self, value):
        self._window = value

        self._disp = self._window._disp
        self._win = self._window._window

        self._init_xevents()
    