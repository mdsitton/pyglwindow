import os
import sys

# These are functions to help with file related tasks

def get_path():
    ''' get the current path '''

    fullPath = os.path.realpath(sys.path[0])
    splitName = fullPath.split('.')
    if 'py' in splitName or 'exe' in splitName:
        fullPath = os.sep.join(fullPath.split(os.sep)[:-1])

    return fullPath

def resolve_path(*location):
	path = get_path()
	location = (path,) + location
	location = os.sep.join(location)

	return location

def resolve_file(location, filename):
	pathInfo = (location, filename)
	filePath = os.sep.join(pathInfo)
	return filePath

def read_file(file):
    with open(file, 'r') as file:
        output = file.read()
    return output
