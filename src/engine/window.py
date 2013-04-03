
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ctypes as ct
import src.engine.bindings.win32 as w32

from src.engine.utils.timehelper import Timer
from src.engine.context import Context
from src.engine.utils.file import get_path

# Constants
FULLSCREEN = 1
WINDOWED = 2
DELTA_TIME = 25  # 25 ms time between updates


class Window(object):
    def __init__(self):

        # Window Styles
        self.fullscreenExStyle = w32.WS_EX_APPWINDOW
        self.fullscreenStyle = w32.WS_POPUP

        self.windowExStyle = (w32.WS_EX_APPWINDOW |
                              w32.WS_EX_WINDOWEDGE)

        self.windowStyle = (w32.WS_OVERLAPPEDWINDOW |
                            w32.WS_CLIPSIBLINGS |
                            w32.WS_CLIPCHILDREN)

        self.windowMode = None

        self.monitorInfo, self.monitorCount = self.get_monitors()

        self.events = {}

        self.timer = Timer()
        self.simulationTime = 0
        self.timeAccumulator = 0

        self.running = True

        self.resize = None

        self.dataPath = get_path() + '\\data'

    def create(self, width, height, fullscreen, title):

        self.startRes = (width, height, fullscreen)

        def wnd_proc(hwnd, message, wParam, lParam):
            if message == w32.WM_SIZE:
                #if wParam == SIZE_MAXIMIZED or wParam == SIZE_RESTORED:
                width = w32.LOWORD(lParam)
                height = w32.HIWORD(lParam)
                # Change this to an event when event system gets coded
                self.resize(width, height)
                return 0
            elif message == w32.WM_CLOSE:
                # TODO - Send an event and let the game code handle when to
                # stop by calling self.window.destroy()
                self.delete()
                return 0
            elif message == w32.WM_KEYDOWN:
                if wParam == w32.VK_F11:
                    if self.windowMode == FULLSCREEN:
                        self.set_window_mode(WINDOWED)
                    elif self.windowMode == WINDOWED:
                        self.set_window_mode(FULLSCREEN)
                    return 0

            return w32.DefWindowProc(hwnd, message, wParam, lParam)

        # create window class
        wndClass = w32.WNDCLASS()
        wndClass.style = w32.CS_HREDRAW | w32.CS_VREDRAW | w32.CS_OWNDC
        wndClass.lpfnWndProc = w32.WNDPROC(wnd_proc)
        wndClass.cbClsExtra = 0
        wndClass.cbWndExtra = 0
        wndClass.hInstance = 0
        wndClass.hIcon = w32.LoadImage(None, self.dataPath + '\\icon.ico', w32.IMAGE_ICON, 16, 16, w32.LR_LOADFROMFILE)# w32.LoadIcon(None, w32.IDI_INFORMATION)
        wndClass.hCursor = w32.LoadCursor(None, w32.IDC_ARROW)
        wndClass.hbrBackground = None
        wndClass.lpszMenuName = None
        wndClass.lpszClassName = 'HelloWin'

        # Register class
        w32.RegisterClass(ct.pointer(wndClass))

        dwExStyle = self.windowExStyle
        dwStyle = self.windowStyle
        self.windowMode = WINDOWED

        # Create window
        self.hwnd = w32.CreateWindowEx(dwExStyle,
                wndClass.lpszClassName,
                title,
                dwStyle,
                w32.CW_USEDEFAULT, w32.CW_USEDEFAULT,
                width, height,
                None, None,
                wndClass.hInstance,
                None)

        self.context = Context(self.hwnd, 3.3)

        self.init()

        self.deviceContext = self.context.get_device_context()

        self.set_window_resolution(width, height)

        if fullscreen is True:
            self.set_window_mode(FULLSCREEN)

        w32.ShowWindow(self.hwnd, w32.SW_SHOWNORMAL)
        w32.SetForegroundWindow(self.hwnd)
        w32.SetFocus(self.hwnd)

        self.resize(width, height)

        msg = w32.MSG()

        while self.running:

            message = w32.PeekMessage(ct.pointer(msg), None, 0, 0, w32.PM_REMOVE)

            if message:
                w32.TranslateMessage(ct.pointer(msg))
                w32.DispatchMessage(ct.pointer(msg))
            else:
                tick = self.timer.tick()
                self.timeAccumulator += tick

                while abs(self.timeAccumulator) >= DELTA_TIME:
                    self.update()
                    self.timeAccumulator -= DELTA_TIME
                    self.simulationTime += DELTA_TIME

                self.render()

    def delete(self):
        ''' Startes the process of exiting '''
        self.destroy()
        self.running = False

    def register_resize(self, func):
        ''' Register the resize function '''
        self.resize = func

    def register_init(self, func):
        ''' register the init function '''
        self.init = func

    def register_render(self, func):
        ''' Register the render function '''
        self.render = func

    def register_update(self, func):
        ''' Register the update function '''
        self.update = func

    def register_destroy(self, func):
        ''' Register the destroy function '''
        self.destroy = func

    def flip(self):
        ''' Swap between the front and back buffers '''
        w32.SwapBuffers(self.deviceContext)

    def get_hwnd(self):
        ''' Return the window's hwnd '''
        return self.hwnd

    def get_monitors(self):

        # Get each monitor and put it into a list
        monitors = []

        def disp_proc(hMonitor, hdcMonitor, lprcMonitor, dwData):
            lprcMonitor = lprcMonitor.contents
            if lprcMonitor.left == 0 and lprcMonitor.top == 0:
                primary = True
            else:
                primary = False

            monitors.append({
                'rect': {
                    'right': lprcMonitor.right,
                    'left': lprcMonitor.left,
                    'top': lprcMonitor.top,
                    'bottom': lprcMonitor.bottom,
                },
                'handle': hMonitor,
                'primary': primary})
            return True

        dispProc = w32.MONITORENUMPROC(disp_proc)
        w32.EnumDisplayMonitors(None, None, dispProc, 0)

        monitorInfo = []
        monitorCount = 0
        for n, mon in enumerate(monitors):
            monitorInfo.append({
                'rect': mon['rect'],
                'handle': mon['handle'],
                'primary': mon['primary'],
                'resolution': {
                    'width': mon['rect']['right'] - mon['rect']['left'],
                    'height': mon['rect']['bottom'] - mon['rect']['top'],
                    'offset': {
                        'x': mon['rect']['left'],
                        'y': mon['rect']['top'],
                    },
                },
            })

            monitorCount += 1

        return monitorInfo, monitorCount

    def get_current_monitor(self, xPos, yPos):

        monitorFound = 0
        for i, monitor in enumerate(self.monitorInfo):
            monRect = monitor['rect']
            if xPos <= monRect['right'] and xPos >= monRect['left']:
                if yPos <= monRect['bottom'] and yPos >= monRect['top']:
                    monitorFound = i

        return monitorFound

    def get_monitor_resolution(self, screenNum):
        """Get the resolution for the specified display."""

        # Select the specified display.
        resolution = self.monitorInfo[screenNum]['resolution']

        return resolution

    def set_monitor_resolution(self, width, height, monitor):
        ''' Changes the resolution of the monitor selected
            This should not be used for the most part
            We do not want to ever change any screen's resolution
            It takes about 3 seconds for the resolution to change
            which is just to long
        '''
        displayDevices = []

        for n in xrange(self.monitorCount):
            displayDevices.append(w32.MONITORINFOEX())
            w32.GetMonitorInfo(self.monitorInfo[monitor]['handle'],
                               ct.pointer(displayDevices[n]))

        screenMode = w32.DEVMODE()

        w32.EnumDisplaySettings(displayDevices[monitor].szDevice,
                                  w32.ENUM_CURRENT_SETTINGS,
                                  ct.pointer(screenMode))

        screenMode.dmSize = ct.sizeof(screenMode)
        screenMode.dmPelsWidth = width
        screenMode.dmPelsHeight = height
        screenMode.dmBitsPerPel = 32
        screenMode.dmFields = (w32.DM_PELSWIDTH |
                               w32.DM_PELSHEIGHT |
                               w32.DM_BITSPERPEL)

        w32.ChangeDisplaySettings(ct.pointer(screenMode), w32.CDS_FULLSCREEN)

        self.monitorInfo, self.monitorCount = self.get_monitors()

    def set_monitor_defaults(self):
        w32.ChangeDisplaySettings(None, w32.CDS_FULLSCREEN)
        self.monitorInfo, self.monitorCount = self.get_monitors()

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
