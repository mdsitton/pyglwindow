import src.library.x11 as x11
from src.engine.utils.types import py_str_to_c
def main():
    display = x11.XOpenDisplay(x11.ct.cast(0, x11.ct.c_char_p))

    defaultScreen = x11.XDefaultScreen(display)

    black = x11.XBlackPixel(display, defaultScreen)

    defaultRoot = x11.XDefaultRootWindow(display)

    window = x11.XCreateSimpleWindow(display, defaultRoot, 0, 0, 200, 100, 0, black, black)
    x11.XSelectInput(display, window, x11.StructureNotifyMask)
    x11.XMapWindow(display, window, defaultRoot)
    x11.XCreateGC(display, window, 0, x11.ct.cast(0, x11.ct.POINTER(x11.XGCValues)))

    print (display, window, defaultScreen, black)

    while True:
        while x11.XPending(display):
            e = x11.XEvent()
            x11.XNextEvent(display, x11.ct.byref(e))
            if e.type == x11.ConfigureNotify:
                print (e.xconfigure.width, e.xconfigure.height)

    x11.XFlush(display)
            
if __name__ == '__main__':
    main()