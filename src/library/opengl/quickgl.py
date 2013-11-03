from src.library.opengl import *

def glGetInteger(item):
    value = c_int(-1)
    glGetIntegerv(item, pointer(value))
    return value.value

def glUniformMatrix4(location, count, transpose, value):
    tempMatrix = (c_float * 4 * 4)()

    for x in range(4):
        for y in range(4):
            tempMatrix[x][y] = value[x][y]

    point = cast(tempMatrix, POINTER(c_float))

    glUniformMatrix4fvARB(location, count, transpose, point)

def glUniformMatrix3(location, count, transpose, value):
    tempMatrix = (c_float * 3 * 3)()

    for x in range(3):
        for y in range(3):
            tempMatrix[x][y] = value[x][y]

    point = cast(tempMatrix, POINTER(c_float))

    glUniformMatrix3fvARB(location, count, transpose, point)
