import ctypes as ct

def cast_ptr(obj, ptrType):
    return ct.cast(obj, ct.POINTER(ptrType))

def convert_list_2d(list, returnType):
    ''' Converts a 2d python list to be used with ctypes '''
    lengthY = len(list)
    lengthX = len(list[0])

    tempList = (ct.c_float * lengthX * lengthY)()

    for y in range(lengthY):
        for x in range(lengthX):
            tempList[y][x] = list[y][x]

    if returnType == 'pointer':
        return cast_ptr(tempList, ct.c_float)
    elif returnType == 'object':
        return tempList

def convert_list(list, returnType):
    ''' Converts a python list to be used with ctypes '''
    length = len(list)

    tempList = (ct.c_float * length)()

    for i in range(length):
        tempList[i] = list[i]

    if returnType == 'pointer':
        return cast_ptr(tempList, ct.c_float)
    elif returnType == 'object':
        return tempList

def py_str_to_c(text):
    '''Converts a python string to a c string'''
    buff = ct.create_string_buffer(text.encode(encoding='UTF-8'))
    c_text = ct.cast(ct.pointer(buff), ct.POINTER(ct.c_char))
    return c_text
py_str_to_c2 = py_str_to_c
