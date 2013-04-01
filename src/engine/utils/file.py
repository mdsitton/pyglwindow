# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import ctypes as ct

# These are functions to help with file related tasks

def get_path():
    fullPath = os.path.realpath(__file__)
    splitPath = fullPath.split('\\')
    
    np = -1
    
    for n, item in enumerate(splitPath):
        if item == 'src':
            pathSection = n
            break
    
    pathLength = len(splitPath)
    return '\\'.join(splitPath[:pathSection])

def read_file(file):
    with open(file, 'r') as file:
        output = file.read()
    
    return output

def py_str_to_c(text):
    buff = ct.create_string_buffer(text)
    c_text = ct.cast(ct.pointer(ct.pointer(buff)), ct.POINTER(ct.POINTER(ct.c_char)))
    return c_text
