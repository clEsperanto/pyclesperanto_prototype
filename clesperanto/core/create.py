from gputools import OCLArray
import numpy as np

def create(dimensions):

    '''
    Convenience method for creating images on the GPU. This method basicall does the same as in CLIJ:

    https://github.com/clij/clij2/blob/master/src/main/java/net/haesleinhuepf/clij2/CLIJ2.java#L156

    :param dimensions: size of the image
    :return: OCLArray, potentially with random values
    '''
    if isinstance(dimensions, OCLArray):
        dimensions = dimensions.shape
    else:
        if (len(dimensions) == 2):
            dimensions = (dimensions[1], dimensions[0])
        else:
            dimensions = (dimensions[2], dimensions[1], dimensions[0])

    return OCLArray.empty(dimensions, np.float32)
