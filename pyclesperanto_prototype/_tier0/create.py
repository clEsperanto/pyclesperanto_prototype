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


def create_like(input: OCLArray):
    return OCLArray.empty(input.shape, np.float32)
