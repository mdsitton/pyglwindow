import src.library.win32 as w32

keymap = {w32.VK_W: 'W', w32.VK_A: 'A', w32.VK_S: 'S', w32.VK_D: 'D', w32.VK_Q: 'Q', w32.VK_E: 'E', 
          w32.VK_F11: 'F11', w32.VK_LEFT: 'LEFT', w32.VK_RIGHT: 'RIGHT', w32.VK_UP: 'UP', w32.VK_DOWN: 'DOWN'}


mousedownmap = {w32.WM_RBUTTONDOWN: 'MOUSE_RIGHT',
                w32.WM_MBUTTONDOWN: 'MOUSE_MIDDLE',
                w32.WM_LBUTTONDOWN: 'MOUSE_LEFT'}
                
mouseupmap = {w32.WM_RBUTTONUP: 'MOUSE_RIGHT',
              w32.WM_MBUTTONUP: 'MOUSE_MIDDLE',
              w32.WM_LBUTTONUP: 'MOUSE_LEFT'}
                    
class Input(object):
    ''' Basic input code to be expanded upon later'''
    def __init__(self):
        self.events = None
    
    def process_input(self, hwnd, message, wParam, lParam):
        if message == w32.WM_KEYDOWN:
            if wParam in keymap.keys():
                prevState = bool((lParam >> 30) & 1)
                if not prevState:
                    self.events.events.append({'event': 'on_keydown', 'data': keymap[wParam]})
        elif message == w32.WM_KEYUP:
            if wParam in keymap.keys():
                self.events.events.append({'event': 'on_keyup', 'data': keymap[wParam]})
        elif message == w32.WM_MOUSEMOVE:
            x = w32.LOWORD(lParam)
            y = w32.HIWORD(lParam)
            self.events.events.append({'event': 'on_mousemove', 'data': [x,y]})
        elif message in mousedownmap.keys():
            self.events.events.append({'event': 'on_mousedown', 'data': mousedownmap[message]})
        elif message in mouseupmap.keys():
            self.events.events.append({'event': 'on_mouseup', 'data': mouseupmap[message]})
        else:
            return False
        return True