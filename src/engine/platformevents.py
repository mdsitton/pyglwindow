

from ctypes import byref

import src.engine.bindings.win32 as w32


class PlatformEvents(object):
    def __init__(self, events):
        self.events = events

    #staticmethod
    def wnd_proc(self, hwnd, message, wParam, lParam):
        if message == w32.WM_SIZE:
            #if wParam == SIZE_MAXIMIZED or wParam == SIZE_RESTORED:
            width = w32.LOWORD(lParam)
            height = w32.HIWORD(lParam)
            
            self.events.append('on_resize', {'width': width, 'height': height})
            
            return 0
        elif message == w32.WM_CLOSE:
            self.events.append('on_close', None)
            return 0
        elif message == w32.WM_PAINT:
            self.events.append('on_paint', None)
        # elif message == w32.WM_KEYDOWN:
            # if wParam == w32.VK_F11:
                # if self.windowMode == FULLSCREEN:
                    # self.set_window_mode(WINDOWED)
                # elif self.windowMode == WINDOWED:
                    # self.set_window_mode(FULLSCREEN)
                # return 0

        return w32.DefWindowProc(hwnd, message, wParam, lParam)

    def get_proc(self):
        return self.win_proc

    def process(self):
        msg = w32.MSG()

        while w32.PeekMessage(byref(msg), None, 0, 0, w32.PM_REMOVE):
            w32.TranslateMessage(byref(msg))
            w32.DispatchMessage(byref(msg))