from .._tier0 import plugin_function
from .._tier0 import create_none
from .._tier0 import create
from .._tier0 import Image
from .._tier0 import execute

@plugin_function(output_creator=create_none)
def n_closest_points(distance_matrix : Image, indexlist_destination : Image = None, n : int = 1, ignore_background : bool = True, ignore_self : bool = True):
    """Determine the n point indices with shortest distance for all points in 
    a distance matrix. 
    
    This corresponds to the n row indices with minimum values for each column of 
    the distance matrix. 
    
    Parameters
    ----------
    distance_matrix : Image
    indexlist_destination : Image
    n : Number
    ignore_background : bool
        The first column and row of the distance matrix will be ignored because they represent the background object.
    ignore_self : bool
        The x==y diagonale will be ignored because it represents the distance of the object to itself.
    
    Returns
    -------
    indexlist_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_nClosestPoints
    """
    from .._tier1 import copy
    from .._tier1 import crop
    from .._tier0 import create
    from .._tier1 import set_column
    from .._tier1 import set_row
    from .._tier1 import set_where_x_equals_y
    from .._tier1 import add_image_and_scalar
    import numpy as np

    max_value = np.finfo(np.float32).max

    if ignore_background:
        distance_matrix = crop(distance_matrix, start_x=1, start_y=1, width=distance_matrix.shape[0] - 1, height=distance_matrix.shape[0] - 1 )

    if ignore_self:
        if not ignore_background:
            distance_matrix = copy(distance_matrix)
        set_where_x_equals_y(distance_matrix, max_value)

    temp = create([int(n), distance_matrix.shape[1]])

    parameters = {
        "src_distancematrix":distance_matrix,
        "dst_indexlist":temp,
    }

    # todo: rename cl-file kernel to fulfill naming conventions
    execute(__file__, "../clij-opencl-kernels/kernels/n_shortest_points_x.cl", "find_n_closest_points", distance_matrix.shape, parameters)

    if (ignore_background):
        indexlist_destination = add_image_and_scalar(temp, indexlist_destination, scalar=1)
    else:
        indexlist_destination = copy(temp, indexlist_destination)

    return indexlist_destination
