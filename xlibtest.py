import src.library.x11 as x11
from src.engine.utils.types import py_str_to_c2

def main():
    display = x11.XOpenDisplay(x11.ct.cast(0, x11.ct.c_char_p))

    defaultScreen = x11.XDefaultScreen(display)

    black = x11.XBlackPixel(display, defaultScreen)

    defaultRoot = x11.XDefaultRootWindow(display)

    window = x11.XCreateSimpleWindow(display, defaultRoot, 0, 0, 200, 100, 0, black, black)
    x11.XSelectInput(display, window, x11.StructureNotifyMask)
    x11.XMapWindow(display, window, defaultRoot)
    x11.XCreateGC(display, window, 0, x11.ct.cast(0, x11.ct.POINTER(x11.XGCValues)))

    wm_delete_window = x11.XInternAtom(display, py_str_to_c2('WM_DELETE_WINDOW'), 0)
    x11.XSetWMProtocols(display, window, x11.ct.pointer(x11.Atom(wm_delete_window)), 1)  # for some reason ctypes converts Atom to int
    running = True
    while running:
        while x11.XPending(display):
            e = x11.XEvent()
            x11.XNextEvent(display, x11.ct.byref(e))
            if e.type == x11.ConfigureNotify:
                print (e.xconfigure.width, e.xconfigure.height)
            elif e.type == x11.ClientMessage:
                if e.xclient.data.l[0] == wm_delete_window:
                    print ('Closing event loop')
                    running = False


    x11.XFlush(display)
            
if __name__ == '__main__':
    main()