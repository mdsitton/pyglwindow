
from ctypes import *
from ctypes.wintypes import *

from src.engine.utils.bindinghelper import define_glext_func

HGLRC = HANDLE

_wglCreateContextAttribsARBParams = (HDC, HGLRC, POINTER(c_int))
wglCreateContextAttribsARB = define_glext_func( 'wglCreateContextAttribsARB', HGLRC, _wglCreateContextAttribsARBParams )