from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def mode_of_touching_neighbors(src_values : Image, touch_matrix : Image, dst_values : Image = None):
    """

    Parameters
    ----------
    src_values
    touch_matrix
    dst_values

    Returns
    -------

    """

    # it is possible to use measurent vectors, which have one element less because they don't
    # contain a measurement for the background
    if touch_matrix.shape[1] == src_values.shape[1] + 1:
        x_correction = -1
    else:
        x_correction = 0

    parameters = {
        "src_values": src_values,
        "src_touch_matrix": touch_matrix,
        "dst_values": dst_values,
        "x_correction": int(x_correction)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/mode_of_touching_neighbors_x.cl', 'mode_of_touching_neighbors', dst_values.shape, parameters)

    return dst_values
