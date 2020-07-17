from ._pycl import OCLArray
import numpy as np


def create(dimensions):

    """
    Convenience method for creating images on the GPU. This method basically does the same as in CLIJ:

    https://github.com/clij/clij2/blob/master/src/main/java/net/haesleinhuepf/clij2/CLIJ2.java#L156

    :param dimensions: size of the image
    :return: OCLArray, potentially with random values
    """

    dimensions = (
        dimensions.shape
        if isinstance(dimensions, OCLArray)
        else tuple(dimensions[::-1])  # reverses a list/tuple
    )
    return OCLArray.empty(dimensions, np.float32)


def create_like(input:OCLArray, input2:OCLArray = None):
    return OCLArray.empty(input.shape, np.float32)

def create_pointlist_from_labelmap(input:OCLArray):
    from .._tier2 import maximum_of_all_pixels
    number_of_labels = int(maximum_of_all_pixels(input))
    number_of_dimensions = len(input.shape)

    return create([number_of_labels, number_of_dimensions])

def create_matrix_from_pointlists(pointlist1:OCLArray, pointlist2:OCLArray):
    width = pointlist1.shape[1] + 1
    height = pointlist2.shape[1] + 1

    return create([width, height])


def create_square_matrix_from_pointlist(pointlist1:OCLArray):
    width = pointlist1.shape[1] + 1

    return create([width, width])


def create_square_matrix_from_labelmap(labelmap: OCLArray):
    from .._tier2 import maximum_of_all_pixels
    width = int(maximum_of_all_pixels(labelmap) + 1)

    return create([width, width])

def create_2d_xy(input):
    return create([input.shape[2], input.shape[1]])
