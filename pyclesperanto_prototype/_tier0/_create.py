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
        else tuple(dimensions)  # reverses a list/tuple
    )
    return OCLArray.empty(dimensions, np.float32)

def create_zyx(dimensions):
    return create(dimensions[::-1])

def create_like(*args):
    dimensions = args[0]
    if isinstance(dimensions, OCLArray):
        dimensions = dimensions.shape
    elif isinstance(dimensions, np.ndarray):
        dimensions = dimensions.shape[::-1]
    return create(dimensions)

def create_pointlist_from_labelmap(input:OCLArray, *args):
    from .._tier2 import maximum_of_all_pixels
    number_of_labels = int(maximum_of_all_pixels(input))
    number_of_dimensions = len(input.shape)
    
    return create([number_of_dimensions, number_of_labels])

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


def create_square_matrix_from_two_labelmaps(labelmap1: OCLArray, labelmap2: OCLArray):
    from .._tier2 import maximum_of_all_pixels
    width = int(maximum_of_all_pixels(labelmap1) + 1)
    height = int(maximum_of_all_pixels(labelmap2) + 1)

    return create([height, width])

def create_2d_xy(input):
    return create([input.shape[2], input.shape[1]])

def create_2d_yx(input):
    return create([input.shape[1], input.shape[2]])

def create_2d_zy(input):
    return create([input.shape[0], input.shape[1]])

def create_2d_zx(input):
    return create([input.shape[0], input.shape[2]])

def create_none(*args):
    return None