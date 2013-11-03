import src.library.x11 as x11
from src.engine.events.base import BaseEvents

class Events(BaseEvents):
    def __init__(self):
        # set from window once game code gives it the events class
        super(Events, self).__init__()

    def process(self):
        e = x11.XEvent()

        while x11.XPending(display):
            x11.XNextEvent(display, x11.ct.byref(e))

            # Current Win32 events captured 
            # if message == w32.WM_SIZE:
            #     self.events.append({'event': 'on_resize', 'data': {'width': width, 'height': height}})
            # elif message == w32.WM_TIMER:
            #     self.append('on_run', None)
            # elif message == w32.WM_CLOSE:
            #    self.append('on_close', None)
            
            self.do_process()