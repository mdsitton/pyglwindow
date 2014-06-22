
import ctypes as ct
from ctypes.util import find_library

import platform

def define_function(libName, name, returnType, params):

    if osName == 'Windows':
        function = ct.WINFUNCTYPE(returnType, *params)
        lib = ct.WinDLL(libName)
    elif osName == 'Darwin' or osName == 'Linux':
        function = ct.CFUNCTYPE(returnType, *params)
        lib = ct.CDLL(find_library(libName))

    address = getattr(lib, name)
    new_func = ct.cast(address, function)

    return new_func


def define_glext_func(name, returnType, params):

    if osName == 'Windows':
        function = ct.WINFUNCTYPE(returnType, *params)
    elif osName == 'Darwin' or osName == 'Linux':
        function = ct.CFUNCTYPE(returnType, *params)
    
    new_func = ct.cast(wglGetProcAddress(name.encode(encoding='UTF-8')), function)

    return new_func

osName = platform.system()
if osName == 'Windows':
    glGetProcAddress = define_function('opengl32', 'wglGetProcAddress', ct.POINTER(ct.c_int), (ct.c_char_p,))
if osName == 'Linux':
    glGetProcAddress = define_function('GL', 'glxGetProcAddress', ct.POINTER(ct.CFUNCTYPE(None)), (ct.POINTER(ct.c_ubyte),))
