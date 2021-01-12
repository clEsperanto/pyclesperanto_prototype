from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def minimum_of_touching_neighbors(values : Image, touch_matrix : Image, minimum_values_destination : Image = None):
    """Takes a touch matrix and a vector of values to determine the minimum 
    value among touching neighbors for every object. 
    
    Parameters
    ----------
    values : Image
        A vector of values corresponding to the labels of which the minimum 
    should be determined.
    touch_matrix : Image
        A touch_matrix specifying which labels are taken into account for 
    neighborhood relationships.
    minimum_values_destination : Image
        A the resulting vector of minimum values in the neighborhood.
     
    
    Returns
    -------
    minimum_values_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimumOfTouchingNeighbors
    """

    # it is possible to use measurent vectors, which have one element less because they don't
    # contain a measurement for the background
    if touch_matrix.shape[1] == values.shape[1] + 1:
        x_correction = -1
    else:
        x_correction = 0

    parameters = {
        "src_values": values,
        "src_touch_matrix": touch_matrix,
        "dst_values": minimum_values_destination,
        "x_correction": int(x_correction)
    }

    # todo: correct kernel function name to fulfill naming conventions
    execute(__file__, '../clij-opencl-kernels/kernels/minimum_of_touching_neighbors_x.cl', 'minimum_value_of_touching_neighbors', minimum_values_destination.shape, parameters)

    return minimum_values_destination
