from .._tier0 import create_matrix_from_pointlists
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_matrix_from_pointlists)
def generate_distance_matrix(coordindate_list1 :Image, coordinate_list2 :Image, distance_matrix_destination :Image = None):
    """Computes the distance between all point coordinates given in two point lists.
    
    Takes two images containing pointlists (dimensionality n * d, n: number of 
    points and d: dimensionality) and builds up a matrix containing the 
    distances between these points. 
    
    Convention: Given two point lists with dimensionality n * d and m * d, the distance 
    matrix will be of size(n + 1) * (m + 1). The first row and column 
    contain zeros. They represent the distance of the objects to a 
    theoretical background object. In that way, distance matrices are of 
    the same size as touch matrices (see generateTouchMatrix). Thus, one 
    can threshold a distance matrix to generate a touch matrix out of it 
    for drawing meshes. 
    
    Parameters
    ----------
    coordinate_list1 : Image
    coordinate_list2 : Image
    distance_matrix_destination : Image
    
    Returns
    -------
    distance_matrix_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.generate_distance_matrix(coordinate_list1, coordinate_list2, distance_matrix_destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_generateDistanceMatrix
    """
    from .._tier1 import set
    set(distance_matrix_destination, 0)

    parameters = {
        "dst_matrix": distance_matrix_destination,
        "src_point_list1": coordindate_list1,
        "src_point_list2": coordinate_list2
    }

    execute(__file__, '../clij-opencl-kernels/kernels/generate_distance_matrix_x.cl', 'generate_distance_matrix', distance_matrix_destination.shape, parameters)

    return distance_matrix_destination