import ctypes as ct

from src.library.x11.x11types import *

from src.engine.utils.bindinghelper import define_function


libgl = "X11"

# Tokens for glXChooseVisual and glXGetConfig:
GLX_USE_GL = 1
GLX_BUFFER_SIZE = 2
GLX_LEVEL = 3
GLX_RGBA = 4
GLX_DOUBLEBUFFER = 5
GLX_STEREO = 6
GLX_AUX_BUFFERS = 7
GLX_RED_SIZE = 8
GLX_GREEN_SIZE = 9
GLX_BLUE_SIZE = 10
GLX_ALPHA_SIZE = 11
GLX_DEPTH_SIZE = 12
GLX_STENCIL_SIZE = 13
GLX_ACCUM_RED_SIZE = 14
GLX_ACCUM_GREEN_SIZE = 15
GLX_ACCUM_BLUE_SIZE = 16
GLX_ACCUM_ALPHA_SIZE = 17

#extern XVisualInfo* glXChooseVisual( Display *dpy, int screen, int *attribList );
glXChooseVisual = define_function(libx11, 'glXChooseVisual', ct.POINTER(XVisualInfo), (ct.POINTER(Display), ct.c_int, ct.POINTER(ct.c_int)))
