from ._pycl import OCLArray
import numpy as np

def create(dimensions):

    '''
    Convenience method for creating images on the GPU. This method basically does the same as in CLIJ:

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


def create_like(input:OCLArray):
    return OCLArray.empty(input.shape, np.float32)

def create_pointlist_from_labelmap(input:OCLArray):
    from .._tier2 import maximum_of_all_pixels
    number_of_labels = int(maximum_of_all_pixels(input))
    number_of_dimensions = len(input.shape)

    return create([number_of_labels, number_of_dimensions])

def create_matrix_from_pointlists(pointlist1:OCLArray, pointlist2:OCLArray):
    width = pointlist1.shape[1]
    height = pointlist2.shape[1]

    print(width)
    print(height)

    return create([width, height])

