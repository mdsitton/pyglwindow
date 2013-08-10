import struct
import sys

PYTHON3 = sys.version_info >= (3, 0)

# Define bytes for python 2.4, 2.5
try:
    bytes = bytes
except NameError:
    bytes = str

# Creating byte strings
if PYTHON3:
    B = lambda x: x.encode('latin1')
else:
    B = lambda x: x

# Operation on bytes
if PYTHON3:
    ord2 = lambda x: x
    chr2 = lambda x: bytes([x])
else:
    ord2 = ord
    chr2 = chr

# Prototype only, not final version
def copyToClassInArray(tempArray, tempClass, inputValues, length):
    j = 0
    for i in xrange(len(tempArray)):
        for property in vars(tempClass).iteritems():
            if j >= length:
                j = 0
            tempArray[i][''.join(property[0])] = inputValues[j]
            j += 1

# Return NULL ended strings
def asciiz(s):
    n = 0
    while (ord2(s[n]) != 0 ):
        n = n + 1

    return s[0:n]

# Range generator
def frange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step