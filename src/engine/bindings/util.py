# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ctypes import *
from ctypes.util import find_library

import platform

class CreateDllFunction(object):
    def __init__(self, libName, name, returnType, params):
    
        if osName == "Windows":
            function = WINFUNCTYPE(returnType, *params)
        elif osName == "Darwin" or osName == "Linux":
            function = CFUNCTYPE(returnType, *params)
            
        address = getattr(self.get_library(libName), name)
        if name == 'glDrawArrays':
            print address
        self.new_func = cast(address, function)
    
    def get_library(self, name):
        if osName == "Windows":
            lib = WinDLL(name)
        elif osName == "Darwin" or osName == "Linux":
            lib = CDLL(find_library(name))
        return lib
    
    def __call__(self, *args, **kwargs):
        return self.new_func(*args, **kwargs)

class CreateFunction(object):
    def __init__(self, name, returnType, params):
        
        if osName == "Windows":
            function = WINFUNCTYPE(returnType, *params)
        elif osName == "Darwin" or osName == "Linux":
            function = CFUNCTYPE(returnType, *params)
        if name == 'glDrawArrays':
            print wglGetProcAddress(name)
        
        self.new_func = cast(wglGetProcAddress(name), function)

    def __call__(self, *args, **kwargs):
        return self.new_func(*args, **kwargs)

osName = platform.system()

wglGetProcAddress = CreateDllFunction('opengl32', 'wglGetProcAddress', POINTER(c_int), (c_char_p,) )