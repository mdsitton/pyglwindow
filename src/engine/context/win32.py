
from src.library.win32 import *
from src.library.opengl.wgl import *
from src.engine.utils.types import cast_ptr


class Context(object):
    ''' Creates and returns an OpenGL Context of the requested version '''

    def __init__(self, oglVersion):

        # Seperate the opengl version into major and minor
        self.major, self.minor = (int(item) for item in str(oglVersion).split('.'))

        # set from window.py when registered from game code
        self.hwnd = None

    def _create(self):
        ''' Called from window code once all values have been set from game code '''

        # Define the wanted Pixel Format
        pfd = self._define_pixel_format()

        self.deviceContext = GetDC(self.hwnd)

        pixelFormat = ChoosePixelFormat(self.deviceContext, pfd)
        SetPixelFormat(self.deviceContext, pixelFormat, pfd)

        if self.major >= 3:

            # We have to import after the initial 2.x context was created
            import src.library.opengl.wglext as wglext
            wglCreateContextAttribsARB = wglext.wglCreateContextAttribsARB

            attribList = (c_int * 7)(WGL_CONTEXT_MAJOR_VERSION_ARB, self.major,
                                     WGL_CONTEXT_MINOR_VERSION_ARB, self.minor,
                                     WGL_CONTEXT_FLAGS_ARB, 0, 0)

            attribList = cast_ptr(attribList, c_int) # Last sorta thing related the ctypes

            self.context = wglCreateContextAttribsARB(self.deviceContext,
                                                      0, attribList)

        else:
            self.context = wglCreateContext(self.deviceContext)

        wglMakeCurrent(self.deviceContext, self.context)

    def _define_pixel_format(self, color=32, depth=24, stencil=8):
        ''' Defines a new pixel format descriptor '''

        pf = PIXELFORMATDESCRIPTOR()
        pf.nVersion = 1
        pf.dwFlags = PFD_DRAW_TO_WINDOW | PFD_SUPPORT_OPENGL | PFD_DOUBLEBUFFER
        pf.iPixelType = PFD_TYPE_RGBA
        pf.cColorBits = color
        pf.cDepthBits = depth
        pf.cStencilBits = stencil
        pf.iLayerType = PFD_MAIN_PLANE

        return pf

    def delete(self):
        ''' Delete's the context '''

        wglMakeCurrent(None, None)
        wglDeleteContext(self.context)
