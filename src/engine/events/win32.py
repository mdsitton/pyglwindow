import src.library.win32 as w32
from src.engine.events.base import BaseEvents

class Events(BaseEvents):

    def wnd_proc(self, hwnd, message, wParam, lParam):
        #print (message)
        if self.type == 'basic':
            return w32.DefWindowProc(hwnd, message, wParam, lParam)
            
        if message == w32.WM_SIZE:
            #if wParam == SIZE_MAXIMIZED or wParam == SIZE_RESTORED:
            width = w32.LOWORD(lParam)
            height = w32.HIWORD(lParam)
            
            self.events.append({'event': 'on_resize', 'data': {'width': width, 'height': height}})
            
        elif message == w32.WM_ENTERSIZEMOVE:
            w32.SetTimer(hwnd, 1, 15, w32.cast(0, w32.TIMERPROC))
        elif message == w32.WM_EXITSIZEMOVE:
            w32.KillTimer(hwnd, 1)
        elif message == w32.WM_TIMER:
            self.events.append({'event': 'on_run', 'data': None})
        elif message == w32.WM_CLOSE:
            self.events.append({'event': 'on_close', 'data': None})
        elif self.input.process_input(hwnd, message, wParam, lParam):
            pass
        else:
            return w32.DefWindowProc(hwnd, message, wParam, lParam)
        
        self.do_process()
        return 0

    def process(self):
        msg = w32.MSG()

        while w32.PeekMessage(msg, None, 0, 0, w32.PM_REMOVE):
            w32.TranslateMessage(msg)
            w32.DispatchMessage(msg)