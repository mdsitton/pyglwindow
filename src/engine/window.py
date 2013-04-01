# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from src.engine.bindings.win32 import *
from src.engine.bindings.opengl import *

        
# Constants
FULLSCREEN = 1
WINDOWED = 2

class WinMain(object):
    def __init__(self):
        
		# Window Styles
        self._fullscreenExStyle = WS_EX_APPWINDOW
        self._fullscreenStyle = WS_POPUP
        
        self._windowExStyle = (WS_EX_APPWINDOW | 
                               WS_EX_WINDOWEDGE)
        
        self._windowStyle = (WS_OVERLAPPEDWINDOW | 
                             WS_CLIPSIBLINGS | 
                             WS_CLIPCHILDREN)
        
        self._windowMode = None
        
        self._monitorInfo, self._monitorCount = self.get_monitors()
        
        self.events = {}
        
    def create(self, width, height, fullscreen, title):
        
        
        self.running = True
        
        def wnd_proc(hwnd, message, wParam, lParam):
            if message == WM_SIZE:
                #if wParam == SIZE_MAXIMIZED or wParam == SIZE_RESTORED:
                width = LOWORD(lParam)
                height = HIWORD(lParam)
                self._resize(width, height) # Change to an event when event system exists
                return 0
            elif message == WM_CLOSE:
                self.running = False # Send an event and let the game code handle when to stop
                return 0
            elif message == WM_KEYDOWN: 
                if wParam == VK_F11:
                    if self._windowMode == FULLSCREEN:
                        self.set_window_mode(WINDOWED)
                    elif self._windowMode == WINDOWED:
                        self.set_window_mode(FULLSCREEN)
            
            return DefWindowProc(hwnd, message, wParam, lParam)
            
        # create window class
        wndClass = WNDCLASS()
        wndClass.style = CS_HREDRAW | CS_VREDRAW | CS_OWNDC
        wndClass.lpfnWndProc = WNDPROC(wnd_proc)
        wndClass.cbClsExtra = 0
        wndClass.cbWndExtra = 0
        wndClass.hInstance = 0
        wndClass.hIcon = LoadIcon(None, IDI_INFORMATION)
        wndClass.hCursor = LoadCursor(None, IDC_ARROW)
        wndClass.hbrBackground = None
        wndClass.lpszMenuName = None
        wndClass.lpszClassName = 'HelloWin'
        
        # Register class
        RegisterClass( byref(wndClass) )
        

        dwExStyle = self._windowExStyle
        dwStyle = self._windowStyle
        self._windowMode = WINDOWED
        
        # Create window
        self._hwnd = CreateWindowEx(dwExStyle,
                wndClass.lpszClassName,
                title,
                dwStyle,
                CW_USEDEFAULT,
                CW_USEDEFAULT,
                width,
                height,
                None,
                None,
                wndClass.hInstance,
                None)
        self.set_window_resolution(width, height)
        
        if fullscreen is True:
            self.set_window_mode(FULLSCREEN)
        
        # Define the wanted Pixel Format
        pfd = PIXELFORMATDESCRIPTOR()
        pfd.nSize = sizeof(pfd)
        pfd.nVersion = 1
        pfd.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER
        pfd.iPixelType = PFD_TYPE_RGBA
        pfd.cColorBits = 32
        pfd.cDepthBits = 24
        pfd.cStencilBits = 8
        pfd.iLayerType = PFD_MAIN_PLANE

        
        self._hdc = GetDC(self._hwnd)
        pixelFormat = ChoosePixelFormat(self._hdc, byref(pfd))
        SetPixelFormat(self._hdc, pixelFormat, byref(pfd))
        
        attribList = (c_int*7)(WGL_CONTEXT_MAJOR_VERSION_ARB, 3,
                               WGL_CONTEXT_MINOR_VERSION_ARB, 3,
                               WGL_CONTEXT_FLAGS_ARB, 0,
                               0)
        
        attribListp = cast(attribList, POINTER(c_int))
        
        hrc = wglCreateContextAttribsARB(self._hdc, 0, attribListp)
        wglMakeCurrent(self._hdc, hrc)
        
        ShowWindow(self._hwnd, SW_SHOWNORMAL)
        SetForegroundWindow(self._hwnd)
        SetFocus(self._hwnd)
        UpdateWindow(self._hwnd)
        self._resize(width, height)
        
        self._init()
        
        msg = MSG()

        while self.running:
            if PeekMessage(byref(msg), None, 0, 0, PM_REMOVE):
                TranslateMessage(byref(msg))
                DispatchMessage(byref(msg))
            else:
                self._update()
                self._render()
        
        wglDeleteContext(hrc)
            
    def register_render(self, func):
        """Register the drawing function"""
        self._render = func
    
    def register_update(self, func):
        """Register the update function"""
        self._update = func
    
    def register_resize(self, func):
        """Register the resize function"""
        self._resize = func

    def register_init(self, func):
        """Register the init function"""
        self._init = func
    
    def flip(self):
        SwapBuffers(self._hdc)
    
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
        
        dispProc = MONITORENUMPROC(disp_proc)
        EnumDisplayMonitors(None, None, dispProc, 0)
        
        monitorInfo = []
        monitorCount = 0
        for n, monitor in enumerate(monitors):
            monitorInfo.append({
                'rect': monitor['rect'],
                'handle': monitor['handle'],
                'primary': monitor['primary'],
                'resolution': {
                    'width': monitor['rect']['right']-monitor['rect']['left'],
                    'height': monitor['rect']['bottom']-monitor['rect']['top'],
                    'offset': {
                        'x': monitor['rect']['left'],
                        'y': monitor['rect']['top'],
                    },
                },
            })
                
            monitorCount += 1
        
        return monitorInfo, monitorCount
    
    def get_current_monitor(self, xPos, yPos):
        
        monitorFound = 0
        for i, monitor in enumerate(self._monitorInfo):
            monRect = monitor['rect']
            if xPos <= monRect['right'] and xPos >= monRect['left']:
                if yPos <= monRect['bottom'] and yPos >= monRect['top']:
                    monitorFound = i
        
        return monitorFound
    
    def get_monitor_resolution(self, screenNum):
        """Get the resolution for the specified display."""
        
        # Select the specified display.
        resolution = self._monitorInfo[screenNum]['resolution']

        return resolution
	
    def set_monitor_resolution(self, width, height, monitor):

        displayDevices = []
        
        print 'cow'
        
        print self._monitorCount
        
        for n in xrange(self._monitorCount):
            displayDevices.append(MONITORINFOEX())
            GetMonitorInfo(self._monitorInfo[monitor]['handle'], byref(displayDevices[n]))

        screenMode = DEVMODE()
        EnumDisplaySettings(displayDevices[monitor].szDevice, ENUM_CURRENT_SETTINGS, pointer(screenMode))
        screenMode.dmSize = sizeof(screenMode)
        screenMode.dmPelsWidth = width
        screenMode.dmPelsHeight = height
        screenMode.dmBitsPerPel = 32
        screenMode.dmFields = DM_PELSWIDTH | DM_PELSHEIGHT | DM_BITSPERPEL
        ChangeDisplaySettings(pointer(screenMode), CDS_FULLSCREEN)
        
        self._monitorInfo, self._monitorCount = self.get_monitors()

    def set_monitor_defaults(self):
        ChangeDisplaySettings(None, CDS_FULLSCREEN)
        self._monitorInfo, self._monitorCount = self.get_monitors()
    
    def get_window_mode(self):
        return self._windowMode
    
    def set_window_mode(self, mode):
        
        resolution = self.get_window_resolution()
        
        width = resolution['x']
        height = resolution['y']
        
        ShowWindow(self._hwnd, SW_HIDE)
        if mode is FULLSCREEN:
            dwExStyle = self._fullscreenExStyle
            dwStyle = self._fullscreenStyle
        else:
            dwExStyle = self._windowExStyle
            dwStyle = self._windowStyle
            self.set_monitor_defaults()
            
        SetWindowLong(self._hwnd, GWL_EXSTYLE, dwExStyle)
        SetWindowLong(self._hwnd, GWL_STYLE, dwStyle)
        self._windowMode = mode
        ShowWindow(self._hwnd, SW_SHOW)
        
        self.set_window_resolution(width, height)
    
    def get_window_resolution(self):
        rcClient = RECT()
        GetClientRect(self._hwnd, byref(rcClient))
        
        return {'x': rcClient.right, 'y': rcClient.bottom}
    
    def set_window_resolution(self, width, height):

        if self._windowMode == FULLSCREEN:
            
            self.set_monitor_resolution(width, height, 0)
                
            # Resize the window to the wanted size, and move it to the wanted location
            MoveWindow(self._hwnd, 0, 0, width, height, False)
            
        elif self._windowMode == WINDOWED:
            # Correct for size issues related to Vista/7/8's window borders
            # Also make the window always start in the center of the monitor
            # that the game was started from
            # Get client rect
            rcClient = RECT()
            GetClientRect(self._hwnd, byref(rcClient))
                
            # Get window rect
            rcWindow = RECT()
            GetWindowRect(self._hwnd, byref(rcWindow))
                
            # Get the screen number that the window has been created on by default
            currentScreen = self.get_current_monitor(rcWindow.left, rcWindow.top)
                
            # Get the window border size
            xDiff = width - rcClient.right
            yDiff = height - rcClient.bottom
                
            # Get the screen resolution
            monitorRes = self.get_monitor_resolution(currentScreen)
    
            # correctly position the monitor in the center of the current screen
            # ox/oy stands for offset x offset y
            xPos = ((monitorRes['width'] - width - xDiff)/2) + monitorRes['offset']['x']
            yPos = ((monitorRes['height'] - height - yDiff)/2) + monitorRes['offset']['y']
                
            # Resize the window to the wanted size, and move it to the wanted location
            MoveWindow(self._hwnd, xPos, yPos, width+xDiff, height+yDiff, False)