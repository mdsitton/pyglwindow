
import src.library.win32 as w32

from src.engine.utils.file import resolve_path
from src.engine.display import Display

# Constants
FULLSCREEN = 1
WINDOWED = 2

class Window(object):
    def __init__(self, width, height, fullscreen, title):
        
        self.title = title
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        
        # Window Styles
        self.fullscreenExStyle = w32.WS_EX_APPWINDOW
        self.fullscreenStyle = w32.WS_POPUP

        self.windowExStyle = (w32.WS_EX_APPWINDOW |
                              w32.WS_EX_WINDOWEDGE)

        self.windowStyle = (w32.WS_OVERLAPPEDWINDOW |
                            w32.WS_CLIPSIBLINGS |
                            w32.WS_CLIPCHILDREN)
        
        self._contextClass = None
        self._context = None
        self._deviceContext = None

        self.events = None

        self._windowMode = None
        
        self.display = Display()

        self.monitorInfo, self.monitorCount = self.display.get_monitors()

        self.dataPath = resolve_path('data')

    def _create(self):

        self.wnd_proc = w32.WNDPROC(self.events.wnd_proc)

        # create window class
        self.wndClass = w32.WNDCLASS()
        self.wndClass.style = w32.CS_HREDRAW | w32.CS_VREDRAW | w32.CS_OWNDC
        self.wndClass.lpfnWndProc = self.wnd_proc
        self.wndClass.cbClsExtra = 0
        self.wndClass.cbWndExtra = 0
        self.wndClass.hInstance = w32.GetModuleHandle(None)
        self.wndClass.hIcon = w32.LoadImage(None, self.dataPath + '\\icon.ico', w32.IMAGE_ICON, 16, 16, w32.LR_LOADFROMFILE)# w32.LoadIcon(None, w32.IDI_INFORMATION)
        self.wndClass.hCursor = w32.LoadCursor(None, w32.IDC_ARROW)
        self.wndClass.hbrBackground = None
        self.wndClass.lpszMenuName = None
        self.wndClass.lpszClassName = 'HelloWin'

        # Register class
        w32.RegisterClass(self.wndClass)

        dwExStyle = self.windowExStyle
        dwStyle = self.windowStyle
        self._windowMode = WINDOWED

        # Create window
        self.hwnd = w32.CreateWindowEx(dwExStyle,
                self.wndClass.lpszClassName,
                self.title,
                dwStyle,
                w32.CW_USEDEFAULT, w32.CW_USEDEFAULT,
                self.width, self.height,
                None, None,
                self.wndClass.hInstance,
                None)

        if self.fullscreen is True:
            self.windowMode = FULLSCREEN

    def delete(self):
        w32.DestroyWindow(self.hwnd)
        w32.UnregisterClass(self.wndClass.lpszClassName, None)

    def __del__(self):
        del self._deviceContext
        del self._context

    def flip(self):
        ''' Swap between the front and back buffers '''
        w32.SwapBuffers(self._deviceContext)

    # Properties for getting the input set
    @property
    def input(self):
        return self._inputClass
    @input.setter
    def input(self, value):
        value.events = self.events
        self._inputClass = value
        self.events.input = value

    # Properties for getting the context setup properly
    @property
    def context(self):
        return self._contextClass
    @context.setter
    def context(self, value):
        self._create()

        self._contextClass = value

        self._contextClass.hwnd = self.hwnd
        self._contextClass._create()

        self._context = self._contextClass.context
        self._deviceContext = self._contextClass.deviceContext
    

    # Properties for getting and setting window visiblity
    @property
    def visibility(self):
        return self._visibility
    @visibility.setter
    def visibility(self, value):
        self._visibility = value
        if value is True:
            w32.ShowWindow(self.hwnd, w32.SW_SHOW)
            w32.SetForegroundWindow(self.hwnd)
            w32.SetFocus(self.hwnd)
        elif value is False:
            w32.ShowWindow(self.hwnd, w32.SW_HIDE)


    # Properties for window mode
    @property
    def mode(self):
        return self._windowMode
    @mode.setter
    def mode(self, wmode):

        width, height = self.windowResolution

        w32.ShowWindow(self.hwnd, w32.SW_HIDE)
        if wmode is FULLSCREEN:
            dwExStyle = self.fullscreenExStyle
            dwStyle = self.fullscreenStyle
        else:
            dwExStyle = self.windowExStyle
            dwStyle = self.windowStyle
            # self.display.set_monitor_defaults()

        w32.SetWindowLong(self.hwnd, w32.GWL_EXSTYLE, dwExStyle)
        w32.SetWindowLong(self.hwnd, w32.GWL_STYLE, dwStyle)

        self._windowMode = wmode

        w32.ShowWindow(self.hwnd, w32.SW_SHOW)

        self.windowResolution = (width, height)


    # Properties for resolution
    @property
    def resolution(self):
        rcClient = w32.RECT()
        w32.GetClientRect(self.hwnd, rcClient)
        return (rcClient.right, rcClient.bottom)
    @resolution.setter
    def resolution(self, value):

        width, height = value
        if self._windowMode == FULLSCREEN:

            self.display.set_monitor_resolution(width, height, 0)

            # Resize the window, and move it to the wanted location
            w32.MoveWindow(self.hwnd, 0, 0, width, height, False)

        elif self._windowMode == WINDOWED:
            # Correct for size issues related to Vista/7/8's window borders
            # Also make the window always start in the center of the monitor
            # that the game was started from
            # Get client rect
            rcClient = w32.RECT()
            w32.GetClientRect(self.hwnd, rcClient)

            # Get window rect
            rcWindow = w32.RECT()
            w32.GetWindowRect(self.hwnd, rcWindow)
            
            # Get the screen number that the window has been created on
            curScreen = self.display.get_current_monitor(rcWindow.left, rcWindow.top)

            # Get the window border size
            xDiff = width - rcClient.right
            yDiff = height - rcClient.bottom
            
            print (xDiff, yDiff)

            # Get the screen resolution
            res = self.display.get_monitor_resolution(curScreen)

            # position the monitor in the center of the current screen
            x = ((res['width'] - width - xDiff) / 2) + res['offset']['x']
            y = ((res['height'] - height - yDiff) / 2) + res['offset']['y']

            # Resize, and move the window to the desired location
            w32.MoveWindow(self.hwnd, x, y, width + xDiff,
                           height + yDiff, False)
