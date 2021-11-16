from ._pycl import OCLArray
import numpy as np
from ._device import Device, get_device

def create(dimensions, dtype=np.float32, device:Device = None):

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
    if device is None:
        device = get_device()
    return device.empty(dimensions, dtype)

def create_zyx(dimensions, device:Device = None):
    return create(dimensions[::-1], device=device)

def create_like(*args, device:Device = None):
    dimensions = args[0]
    if isinstance(dimensions, OCLArray):
        dimensions = dimensions.shape
    elif isinstance(dimensions, np.ndarray):
        dimensions = dimensions.shape[::-1]
    return create(dimensions, device=device)

def create_binary_like(*args, device:Device = None):
    dimensions = args[0]
    if isinstance(dimensions, OCLArray):
        dimensions = dimensions.shape
    elif isinstance(dimensions, np.ndarray):
        dimensions = dimensions.shape[::-1]
    return create(dimensions, np.uint8, device=device)

def create_labels_like(*args, device:Device = None):
    dimensions = args[0]
    if isinstance(dimensions, OCLArray):
        dimensions = dimensions.shape
    elif isinstance(dimensions, np.ndarray):
        dimensions = dimensions.shape[::-1]
    return create(dimensions, np.uint32, device=device)

def create_pointlist_from_labelmap(input:OCLArray, *args, device:Device = None):
    from .._tier2 import maximum_of_all_pixels
    number_of_labels = int(maximum_of_all_pixels(input))
    number_of_dimensions = len(input.shape)
    
    return create([number_of_dimensions, number_of_labels], device=device)

def create_vector_from_labelmap(input: OCLArray, *args, device:Device = None):
    from .._tier2 import maximum_of_all_pixels
    number_of_labels = int(maximum_of_all_pixels(input)) + 1

    return create([1, number_of_labels], device=device)

def create_matrix_from_pointlists(pointlist1:OCLArray, pointlist2:OCLArray, device:Device = None):
    width = pointlist1.shape[1] + 1
    height = pointlist2.shape[1] + 1

    return create([width, height], device=device)

def create_from_pointlist(pointlist: OCLArray, *args, device:Device = None):
    from .._tier1 import maximum_x_projection
    from .._tier0 import pull

    max_pos = pull(maximum_x_projection(pointlist)).T.astype(int)
    max_pos = max_pos[0]

    if len(max_pos) == 3:  # 3D image requested
        destination = create([max_pos[2] + 1, max_pos[1] + 1, max_pos[0] + 1], device=device)
    elif len(max_pos) == 2:  # 2D image requested
        destination = create([max_pos[1] + 1, max_pos[0] + 1], device=device)
    else:
        raise Exception("Size not supported: " + str(max_pos))
    return destination

def create_square_matrix_from_pointlist(pointlist1:OCLArray, device:Device = None):
    width = pointlist1.shape[1] + 1

    return create([width, width], device=device)


def create_square_matrix_from_labelmap(labelmap: OCLArray, device:Device = None):
    from .._tier2 import maximum_of_all_pixels
    width = int(maximum_of_all_pixels(labelmap) + 1)

    return create([width, width], device=device)


def create_square_matrix_from_two_labelmaps(labelmap1: OCLArray, labelmap2: OCLArray, device:Device = None):
    from .._tier2 import maximum_of_all_pixels
    width = int(maximum_of_all_pixels(labelmap1) + 1)
    height = int(maximum_of_all_pixels(labelmap2) + 1)

    return create([height, width],device=device)


def create_vector_from_square_matrix(square_matrix : OCLArray, *args, device:Device = None):
    return create([1, square_matrix.shape[0]], device=device)


def create_2d_xy(input, device:Device = None):
    if len(input.shape) == 3:
        return create([input.shape[2], input.shape[1]], device=device)
    else:
        return create([input.shape[1], input.shape[0]], device=device)

def create_2d_yx(input, device:Device = None):
    if len(input.shape) == 3:
        return create([input.shape[1], input.shape[2]], device=device)
    else:
        return create([input.shape[0], 1], device=device)

def create_2d_zy(input, device:Device = None):
    if len(input.shape) == 3:
        return create([input.shape[0], input.shape[1]], device=device)
    else:
        return create([1, input.shape[0]], device=device)

def create_2d_yz(input, device:Device = None):
    if len(input.shape) == 3:
        return create([input.shape[1], input.shape[0]], device=device)
    else:
        return create([input.shape[0], 1], device=device)

def create_2d_zx(input, device:Device = None):
    if len(input.shape) == 3:
        return create([input.shape[0], input.shape[2]], device=device)
    else:
        return create([1, input.shape[1]], device=device)

def create_2d_xz(input, device:Device = None):
    if len(input.shape) == 3:
        return create([input.shape[2], input.shape[0]], device=device)
    else:
        return create([input.shape[1], 1], device=device)

def create_none(*args, device:Device = None):
    return None