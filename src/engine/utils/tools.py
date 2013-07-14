
import struct

# Prototype only, not final version
def copyToClassInArray(tempArray, tempClass, inputValues, length):
    j = 0
    for i in range(len(tempArray)):
        for property in vars(tempClass).iteritems():
            if j >= length:
                j = 0
            tempArray[i][''.join(property[0])] = inputValues[j]
            j += 1