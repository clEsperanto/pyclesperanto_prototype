import numpy as np
from gputools import OCLArray

def push(nparray):
    '''
    converts a numpy array to an OpenCL array

    This method does the same as the converters in CLIJ but is less flexible
    https://github.com/clij/clij-core/tree/master/src/main/java/net/haesleinhuepf/clij/converters/implementations

    :param nparray: input numpy array
    :return: opencl-array
    '''

    if (isinstance(nparray, OCLArray)):
        return nparray

    temp = nparray.astype(np.float32)
    #print("tmep: ")
    #print(temp)

    if (len(temp.shape) == 2):
        temp = np.swapaxes(temp, 0, 1)
    else:
        temp = np.swapaxes(temp, 0, 2)

    temp2 = OCLArray.from_array(temp)
    return temp2

def push_zyx(nparray):
    if (isinstance(nparray, OCLArray)):
        return nparray

    temp = nparray.astype(np.float32)
    return OCLArray.from_array(temp)
