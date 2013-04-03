# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ctypes import *
from ctypes.util import find_library

import platform


def CreateDllFunction(libName, name, returnType, params):

    if osName == "Windows":
        function = WINFUNCTYPE(returnType, *params)
        lib = WinDLL(libName)
    elif osName == "Darwin" or osName == "Linux":
        function = CFUNCTYPE(returnType, *params)
        lib = CDLL(find_library(libName))

    address = getattr(lib, name)
    new_func = cast(address, function)

    return new_func


def CreateFunction(name, returnType, params):

    if osName == "Windows":
        function = WINFUNCTYPE(returnType, *params)
    elif osName == "Darwin" or osName == "Linux":
        function = CFUNCTYPE(returnType, *params)

    new_func = cast(wglGetProcAddress(name), function)

    return new_func

osName = platform.system()

wglGetProcAddress = CreateDllFunction('opengl32', 'wglGetProcAddress', POINTER(c_int), (c_char_p,))
