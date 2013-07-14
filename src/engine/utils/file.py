
import os
import ctypes as ct

# These are functions to help with file related tasks

def get_path():
    fullPath = os.path.realpath(__file__)
    splitPath = fullPath.split('\\')

    np = -1.

    frozen = False

    for n, item in enumerate(splitPath):
        if item in ('library.zip', 'src', 'launcher.exe'):
            pathSection = n
            break

    pathLength = len(splitPath)
    return '\\'.join(splitPath[:pathSection])

def read_file(file):
    with open(file, 'r') as file:
        output = file.read()
    return output
