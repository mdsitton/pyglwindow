import ctypes as ct

from src.library.x11.x11types import *

from src.engine.utils.bindinghelper import define_function


libgl = "GL"

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


# Error codes returned by glXGetConfig:
GLX_BAD_SCREEN = 1
GLX_BAD_ATTRIBUTE = 2
GLX_NO_EXTENSION = 3
GLX_BAD_VISUAL = 4
GLX_BAD_CONTEXT = 5
GLX_BAD_VALUE = 6
GLX_BAD_ENUM = 7


# GLX 1.1 and later:
GLX_VENDOR = 1
GLX_VERSION = 2
GLX_EXTENSIONS = 3


# GLX 1.3 and later:
GLX_CONFIG_CAVEAT = 0x20
GLX_DONT_CARE = 0xFFFFFFFF
GLX_X_VISUAL_TYPE = 0x22
GLX_TRANSPARENT_TYPE = 0x23
GLX_TRANSPARENT_INDEX_VALUE = 0x24
GLX_TRANSPARENT_RED_VALUE = 0x25
GLX_TRANSPARENT_GREEN_VALUE = 0x26
GLX_TRANSPARENT_BLUE_VALUE = 0x27
GLX_TRANSPARENT_ALPHA_VALUE = 0x28
GLX_WINDOW_BIT = 0x00000001
GLX_PIXMAP_BIT = 0x00000002
GLX_PBUFFER_BIT = 0x00000004
GLX_AUX_BUFFERS_BIT = 0x00000010
GLX_FRONT_LEFT_BUFFER_BIT = 0x00000001
GLX_FRONT_RIGHT_BUFFER_BIT = 0x00000002
GLX_BACK_LEFT_BUFFER_BIT = 0x00000004
GLX_BACK_RIGHT_BUFFER_BIT = 0x00000008
GLX_DEPTH_BUFFER_BIT = 0x00000020
GLX_STENCIL_BUFFER_BIT = 0x00000040
GLX_ACCUM_BUFFER_BIT = 0x00000080
GLX_NONE = 0x8000
GLX_SLOW_CONFIG = 0x8001
GLX_TRUE_COLOR = 0x8002
GLX_DIRECT_COLOR = 0x8003
GLX_PSEUDO_COLOR = 0x8004
GLX_STATIC_COLOR = 0x8005
GLX_GRAY_SCALE = 0x8006
GLX_STATIC_GRAY = 0x8007
GLX_TRANSPARENT_RGB = 0x8008
GLX_TRANSPARENT_INDEX = 0x8009
GLX_VISUAL_ID = 0x800B
GLX_SCREEN = 0x800C
GLX_NON_CONFORMANT_CONFIG = 0x800D
GLX_DRAWABLE_TYPE = 0x8010
GLX_RENDER_TYPE = 0x8011
GLX_X_RENDERABLE = 0x8012
GLX_FBCONFIG_ID = 0x8013
GLX_RGBA_TYPE = 0x8014
GLX_COLOR_INDEX_TYPE = 0x8015
GLX_MAX_PBUFFER_WIDTH = 0x8016
GLX_MAX_PBUFFER_HEIGHT = 0x8017
GLX_MAX_PBUFFER_PIXELS = 0x8018
GLX_PRESERVED_CONTENTS = 0x801B
GLX_LARGEST_PBUFFER = 0x801C
GLX_WIDTH = 0x801D
GLX_HEIGHT = 0x801E
GLX_EVENT_MASK = 0x801F
GLX_DAMAGED = 0x8020
GLX_SAVED = 0x8021
GLX_WINDOW = 0x8022
GLX_PBUFFER = 0x8023
GLX_PBUFFER_HEIGHT = 0x8040
GLX_PBUFFER_WIDTH = 0x8041
GLX_RGBA_BIT = 0x00000001
GLX_COLOR_INDEX_BIT = 0x00000002
GLX_PBUFFER_CLOBBER_MASK = 0x08000000


# GLX 1.4 and later:
GLX_SAMPLE_BUFFERS = 0x186a0
GLX_SAMPLES = 0x186a1

noParams = ()

# GLX 1.0
glXChooseVisual = define_function(libgl, 'glXChooseVisual', ct.POINTER(XVisualInfo), (ct.POINTER(Display), ct.c_int, ct.POINTER(ct.c_int)))
glXCreateContext = define_function(libgl, 'glXCreateContext', GLXContext, ( ct.POINTER(Display), ct.POINTER(XVisualInfo), GLXContext, Bool ) )
glXDestroyContext = define_function(libgl, 'glXDestroyContext', None, ( ct.POINTER(Display), GLXContext ) )
glXMakeCurrent = define_function(libgl, 'glXMakeCurrent', Bool, ( ct.POINTER(Display), GLXDrawable, GLXContext ) )
glXCopyContext = define_function(libgl, 'glXCopyContext', None, ( ct.POINTER(Display), GLXContext, GLXContext, ct.c_ulong ) )
glXSwapBuffers = define_function(libgl, 'glXSwapBuffers', None, ( ct.POINTER(Display), GLXDrawable ) )
glXCreateGLXPixmap = define_function(libgl, 'glXCreateGLXPixmap', GLXPixmap, ( ct.POINTER(Display), ct.POINTER(XVisualInfo), Pixmap ) )
glXDestroyGLXPixmap = define_function(libgl, 'glXDestroyGLXPixmap', None, ( ct.POINTER(Display), GLXPixmap ) )
glXQueryExtension = define_function(libgl, 'glXQueryExtension', Bool, ( ct.POINTER(Display), ct.POINTER(ct.c_int), ct.POINTER(ct.c_int)) )
glXQueryVersion = define_function(libgl, 'glXQueryVersion', Bool, ( ct.POINTER(Display), ct.POINTER(ct.c_int), ct.POINTER(ct.c_int)) )
glXIsDirect = define_function(libgl, 'glXIsDirect', Bool, ( ct.POINTER(Display), GLXContext ) )
glXGetConfig = define_function(libgl, 'glXGetConfig', ct.c_int, ( ct.POINTER(Display), ct.POINTER(XVisualInfo), ct.c_int, ct.POINTER(ct.c_int)) )
glXGetCurrentContext = define_function(libgl, 'glXGetCurrentContext', GLXContext, noParams )
glXGetCurrentDrawable = define_function(libgl, 'glXGetCurrentDrawable', GLXDrawable, noParams )
glXWaitGL = define_function(libgl, 'glXWaitGL', None, noParams )
glXWaitX = define_function(libgl, 'glXWaitX', None, noParams)
glXUseXFont = define_function(libgl, 'glXUseXFont', None, ( Font, ct.c_int, ct.c_int, ct.c_int ) )


# GLX 1.1 and later
glXQueryExtensionsString = define_function(libgl, 'glXQueryExtensionsString',ct.POINTER(ct.c_char), ( ct.POINTER(Display), ct.c_int ) )
glXQueryServerString = define_function(libgl, 'glXQueryServerString',ct.POINTER(ct.c_char), ( ct.POINTER(Display), ct.c_int, ct.c_int ) )
glXGetClientString = define_function(libgl, 'glXGetClientString',ct.POINTER(ct.c_char), ( ct.POINTER(Display), ct.c_int ) )

# GLX 1.2 and later
glXGetCurrentDisplay = define_function(libgl, 'glXGetCurrentDisplay',ct.POINTER(Display), noParams )

# GLX 1.3 and later
glXChooseFBConfig = define_function(libgl, 'glXChooseFBConfig',ct.POINTER(GLXFBConfig), ( ct.POINTER(Display), ct.c_int, ct.POINTER(ct.c_int), ct.POINTER(ct.c_int) ) )
glXGetFBConfigAttrib = define_function(libgl, 'glXGetFBConfigAttrib', ct.c_int, ( ct.POINTER(Display), GLXFBConfig, ct.c_int, ct.POINTER(ct.c_int) ) )
glXGetFBConfigs = define_function(libgl, 'glXGetFBConfigs',ct.POINTER(GLXFBConfig), ( ct.POINTER(Display), ct.c_int, ct.POINTER(ct.c_int) ) )
glXGetVisualFromFBConfig = define_function(libgl, 'glXGetVisualFromFBConfig',ct.POINTER(XVisualInfo), ( ct.POINTER(Display), GLXFBConfig ) )
glXCreateWindow = define_function(libgl, 'glXCreateWindow', GLXWindow, ( ct.POINTER(Display), GLXFBConfig, Window, ct.POINTER(ct.c_int) ) )
glXDestroyWindow = define_function(libgl, 'glXDestroyWindow', None, ( ct.POINTER(Display), GLXWindow ) )
glXCreatePixmap = define_function(libgl, 'glXCreatePixmap', GLXPixmap, ( ct.POINTER(Display), GLXFBConfig, Pixmap, ct.POINTER(ct.c_int) ) )
glXDestroyPixmap = define_function(libgl, 'glXDestroyPixmap', None, ( ct.POINTER(Display), GLXPixmap ) )
glXCreatePbuffer = define_function(libgl, 'glXCreatePbuffer', GLXPbuffer, ( ct.POINTER(Display), GLXFBConfig, ct.POINTER(ct.c_int) ) )
glXDestroyPbuffer = define_function(libgl, 'glXDestroyPbuffer', None, ( ct.POINTER(Display), GLXPbuffer ) )
glXQueryDrawable = define_function(libgl, 'glXQueryDrawable', None, ( ct.POINTER(Display), GLXDrawable, ct.c_int, ct.POINTER(ct.c_uint) ) )
glXCreateNewContext = define_function(libgl, 'glXCreateNewContext', GLXContext, ( ct.POINTER(Display), GLXFBConfig, ct.c_int, GLXContext, Bool ) )
glXMakeContextCurrent = define_function(libgl, 'glXMakeContextCurrent', Bool, ( ct.POINTER(Display), GLXDrawable, GLXDrawable, GLXContext ) )
glXGetCurrentReadDrawable = define_function(libgl, 'glXGetCurrentReadDrawable', GLXDrawable, noParams )
glXQueryContext = define_function(libgl, 'glXQueryContext', ct.c_int, ( ct.POINTER(Display), GLXContext, ct.c_int, ct.POINTER(ct.c_int) ) )
glXSelectEvent = define_function(libgl, 'glXSelectEvent', None, ( ct.POINTER(Display), GLXDrawable, ct.c_ulong ) )
glXGetSelectedEvent = define_function(libgl, 'glXGetSelectedEvent', None, ( ct.POINTER(Display), GLXDrawable, ct.POINTER(ct.c_ulong)) )