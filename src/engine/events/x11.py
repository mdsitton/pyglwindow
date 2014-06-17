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

            if e.type == x11.ConfigureNotify:
                width = e.xconfigure.width
                height = e.xconfigure.height

                self.events.append({'event': 'on_resize', 'data': {'width': width, 'height': height}})
                self.events.append({'event': 'on_run', 'data': None})
            elif e.type == x11.ClientMessage:
                if e.xclient.data.l[0] == wm_delete_window:
                    self.events.append({'event': 'on_close', 'data': None})
            
            self.do_process()