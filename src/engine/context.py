# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from src.engine.bindings.win32 import *
from src.engine.bindings.opengl.wgl import *
from src.engine.utils.types import castPtr


class Context(object):
    ''' Creates and returns an OpenGL Context of the requested version '''

    def __init__(self, hwnd, oglVersion):

        # Seperate the opengl version into major and minor
        major, minor = (int(item) for item in str(oglVersion).split('.'))

        # Define the wanted Pixel Format
        pfd = self.define_pixel_format()

        self.deviceContext = GetDC(hwnd)

        pixelFormat = ChoosePixelFormat(self.deviceContext, pointer(pfd))
        SetPixelFormat(self.deviceContext, pixelFormat, pointer(pfd))

        if major >= 3:

            # We have to import after the initial 2.x context was created
            import src.engine.bindings.opengl.wglext as wglext
            wglCreateContextAttribsARB = wglext.wglCreateContextAttribsARB

            attribList = (c_int * 7)(WGL_CONTEXT_MAJOR_VERSION_ARB, major,
                                     WGL_CONTEXT_MINOR_VERSION_ARB, minor,
                                     WGL_CONTEXT_FLAGS_ARB, 0, 0)

            attribList = castPtr(attribList, c_int)

            self.context = wglCreateContextAttribsARB(self.deviceContext,
                                                      0, attribList)

        else:
            self.context = wglCreateContext(self.deviceContext)

        wglMakeCurrent(self.deviceContext, self.context)

    def define_pixel_format(self, color=32, depth=24, stencil=8):
        ''' Defines a new pixel format descriptor '''

        pf = PIXELFORMATDESCRIPTOR()
        pf.nSize = sizeof(pf)
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

    def get_context(self):
        ''' Returns the rendering context '''
        return self.context

    def get_device_context(self):
        return self.deviceContext