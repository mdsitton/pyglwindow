
import ctypes as ct
import src.engine.bindings.win32 as w32

from src.engine.utils.timehelper import Timer
from src.engine.context import Context
from src.engine.utils.file import get_path
from src.engine.display import Display
from src.engine.utils.instancetracker import InstanceTracker

# Constants
FULLSCREEN = 1
WINDOWED = 2

class Window(object):
    def __init__(self, width, height, fullscreen, title, oglversion):
        
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        
        self._createdEventSystem = False
        
        self.events = InstanceTracker.get('Events')
        
        
        # If there is no current event instance create one
        if not self.events:
            from src.engine.events import Events
            
            self.events = Events()
            self._createdEventSystem = True
            InstanceTracker.set(self.events)
        
        
        self.platformevents = InstanceTracker.get('PlatformEvents')
        
        self.wnd_proc = w32.WNDPROC(self.platformevents.wnd_proc)
        
        # Window Styles
        self.fullscreenExStyle = w32.WS_EX_APPWINDOW
        self.fullscreenStyle = w32.WS_POPUP

        self.windowExStyle = (w32.WS_EX_APPWINDOW |
                              w32.WS_EX_WINDOWEDGE)

        self.windowStyle = (w32.WS_OVERLAPPEDWINDOW |
                            w32.WS_CLIPSIBLINGS |
                            w32.WS_CLIPCHILDREN)

        self.windowMode = None
        
        self.display = Display()

        self.monitorInfo, self.monitorCount = self.display.get_monitors()

        self.dataPath = get_path() + '\\data'

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
        w32.RegisterClass(ct.byref(self.wndClass))

        dwExStyle = self.windowExStyle
        dwStyle = self.windowStyle
        self.windowMode = WINDOWED

        # Create window
        self.hwnd = w32.CreateWindowEx(dwExStyle,
                self.wndClass.lpszClassName,
                title,
                dwStyle,
                w32.CW_USEDEFAULT, w32.CW_USEDEFAULT,
                width, height,
                None, None,
                self.wndClass.hInstance,
                None)

        if fullscreen is True:
            self.set_window_mode(FULLSCREEN)
        
        
        self.context = Context(self, oglversion)
        self.deviceContext = self.context.get_device_context()
    
    def __del__(self):
        print ('cow')
        # Remove the event system if it was created here
        if self._createdEventSystem:
            InstanceTracker.remove(self.events)
        print ('cow3')
        del self.deviceContext
        del self.context
        w32.DestroyWindow(self.hwnd)
        w32.UnregisterClass(self.winClass.lpszClassName, None)

    def flip(self):
        ''' Swap between the front and back buffers '''
        w32.SwapBuffers(self.deviceContext)

    def get_window(self):
        ''' Return the window's platform specific id '''
        return self.hwnd
    
    def get_visibility(self, visibility):
        return self.visibility
    
    def set_visibility(self, visibility):
        ''' Sets the window to the specified visibility '''
        self.visibility = visibility
        if visibility is True:
            w32.ShowWindow(self.hwnd, w32.SW_SHOW)
            w32.SetForegroundWindow(self.hwnd)
            w32.SetFocus(self.hwnd)
        elif visibility is False:
            w32.ShowWindow(self.hwnd, w32.SW_HIDE)

    def get_window_mode(self):
        return self.windowMode

    def set_window_mode(self, mode):

        resolution = self.get_window_resolution()

        width = resolution['x']
        height = resolution['y']

        w32.ShowWindow(self.hwnd, w32.SW_HIDE)
        if mode is FULLSCREEN:
            dwExStyle = self.fullscreenExStyle
            dwStyle = self.fullscreenStyle
        else:
            dwExStyle = self.windowExStyle
            dwStyle = self.windowStyle
            self.set_monitor_defaults()

        w32.SetWindowLong(self.hwnd, w32.GWL_EXSTYLE, dwExStyle)
        w32.SetWindowLong(self.hwnd, w32.GWL_STYLE, dwStyle)
        self.windowMode = mode
        w32.ShowWindow(self.hwnd, w32.SW_SHOW)

        self.set_window_resolution(width, height)

    def get_window_resolution(self):
        rcClient = w32.RECT()
        w32.GetClientRect(self.hwnd, ct.byref(rcClient))

        return {'x': rcClient.right, 'y': rcClient.bottom}

    def set_window_resolution(self, width, height):

        if self.windowMode == FULLSCREEN:

            self.set_monitor_resolution(width, height, 0)

            # Resize the window, and move it to the wanted location
            w32.MoveWindow(self.hwnd, 0, 0, width, height, False)

        elif self.windowMode == WINDOWED:
            # Correct for size issues related to Vista/7/8's window borders
            # Also make the window always start in the center of the monitor
            # that the game was started from
            # Get client rect
            rcClient = w32.RECT()
            w32.GetClientRect(self.hwnd, ct.byref(rcClient))

            # Get window rect
            rcWindow = w32.RECT()
            w32.GetWindowRect(self.hwnd, ct.byref(rcWindow))

            # Get the screen number that the window has been created on
            curScreen = self.get_current_monitor(rcWindow.left, rcWindow.top)

            # Get the window border size
            xDiff = width - rcClient.right
            yDiff = height - rcClient.bottom

            # Get the screen resolution
            res = self.get_monitor_resolution(curScreen)

            # position the monitor in the center of the current screen
            x = ((res['width'] - width - xDiff) / 2) + res['offset']['x']
            y = ((res['height'] - height - yDiff) / 2) + res['offset']['y']

            # Resize, and move the window to the desired location
            w32.MoveWindow(self.hwnd, x, y, width + xDiff,
                           height + yDiff, False)
