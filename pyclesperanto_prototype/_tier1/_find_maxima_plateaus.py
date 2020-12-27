from warnings import warn

from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def find_maxima_plateaus(source: Image, destination:Image, dimension : int = None):
    """
    Finds local maxima, which might be groups of pixels with the same intensity and marks them in a binary image.
    In order to do this, it iterates over all pixels in a given dimension (e.g. from left to right) and searches for
    maximum-plateaus. If no dimension is specified, to does that in all directsion subsequently and returns the binary
    intersection (binary-AND) of the 2 or 3 intermediate results.

    Parameters
    ----------
    source : Image
        intensity image or distance map where local maxima should be found
    destination
        binary image with pixels which belong to local maximum plateaus
    dimension : int
        x = 0, y = 1, z = 2

    Returns
    -------
        destination
    """
    from .._tier0 import create_like
    from .._tier1 import binary_and
    from .._tier1 import copy
    from .._tier1 import set

    if dimension is None:
        width = destination.shape[-1]
        height = destination.shape[-2]
        if len(destination.shape) > 2:
            depth = destination[0]
        else:
            depth = 1

        print("whd", width, height, depth)

        result = None

        if width > 1:
            result = create_like(destination)
            find_maxima_plateaus(source, result, 0)

        if height > 1:
            temp1 = create_like(destination)
            find_maxima_plateaus(source, temp1, 1)

            if result is None:
                result = temp1
            else:
                temp2 = create_like(destination)
                binary_and(result, temp1, temp2)
                # temp1.close();
                # result.close();
                result = temp2

        if depth > 1:
            if result is None:
                find_maxima_plateaus(source, destination, 2)
            else:
                temp1 = create_like(destination)
                find_maxima_plateaus(source, temp1, 2)
                binary_and(result, temp1, destination)

                # temp1.close();
                # result.close();
        else:
            if result is not None:
                copy(result, destination)
            else:
                warn("find maxima plateaus was processing single pixel image and did not find maxima")
                set(destination, 0)

    else:
        parameters = {
            "src":source,
            "dst":destination
        }

        global_sizes = list(destination.shape)
        global_sizes.reverse()

        if dimension == 0:
            global_sizes[0] = 1
            global_sizes.reverse()
            execute(__file__, 'find_maxima_plateaus_1d_x.cl', 'find_maxima_plateaus_1d_x', global_sizes, parameters)
        elif dimension == 1:
            global_sizes[1] = 1
            global_sizes.reverse()
            execute(__file__, 'find_maxima_plateaus_1d_x.cl', 'find_maxima_plateaus_1d_y', global_sizes, parameters)
        elif dimension == 2:
            global_sizes[2] = 1
            global_sizes.reverse()
            execute(__file__, 'find_maxima_plateaus_1d_x.cl', 'find_maxima_plateaus_1d_z', global_sizes, parameters)

        #print("---------------")
        #print("FMP ", dimension)
        #print(destination)
        #print("---------------")

    return destination
