from src.engine.bindings.win32 import *
from src.engine.bindings.opengl.wgl import *

class Context(object):
    def __init__(self):
        # create window class
        wndClass = WNDCLASS()
        wndClass.style = CS_HREDRAW | CS_VREDRAW | CS_OWNDC
        wndClass.lpfnWndProc = WNDPROC(self.wnd_proc)
        wndClass.cbClsExtra = 0
        wndClass.cbWndExtra = 0
        wndClass.hInstance = 0
        wndClass.hIcon = LoadIcon(None, IDI_INFORMATION)
        wndClass.hCursor = LoadCursor(None, IDC_ARROW)
        wndClass.hbrBackground = None
        wndClass.lpszMenuName = None
        wndClass.lpszClassName = 'tempContext'

        # Register class
        RegisterClass( byref(wndClass) )

        dwStyle = (WS_OVERLAPPEDWINDOW | 
                   WS_CLIPSIBLINGS | 
                   WS_CLIPCHILDREN)

        # Create window
        self._hwnd = CreateWindowEx(WS_EX_APPWINDOW, wndClass.lpszClassName, 
                    'tempContext', dwStyle, CW_USEDEFAULT, CW_USEDEFAULT, 0, 0, None, 
                    None, wndClass.hInstance, None)

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
        self._hrc = wglCreateContext(self._hdc)
        wglMakeCurrent(self._hdc, self._hrc)

    def wnd_proc( self, hwnd, message, wParam, lParam):
        return DefWindowProc(hwnd, message, wParam, lParam)
        
    def destroy(self):
        wglMakeCurrent(None, None)
        wglDeleteContext(self._hrc)