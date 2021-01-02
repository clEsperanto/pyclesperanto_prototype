from .._tier0 import create_matrix_from_pointlists
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_matrix_from_pointlists)
def generate_angle_matrix(coordinate_list1 :Image, coordinate_list2 :Image, angle_matrix_destination :Image = None):
    """Computes the angle in radians between all point coordinates given in two point lists.
    
    Takes two images containing pointlists (dimensionality n * d, n: number of 
    points and d: dimensionality) and builds up a matrix containing the 
    angles between these points.

    Convention: Values range from -90 to 90 degrees (-0.5 to 0.5 pi radians)
    * -90 degreess (-0.5 pi radians): Top
    * 0 defrees (0 radians): Right
    * 90 degrees (0.5 pi radians): Bottom

    Convention: Given two point lists with dimensionality n * d and m * d, the distance 
    matrix will be of size(n + 1) * (m + 1). The first row and column 
    contain zeros. They represent the distance of the objects to a 
    theoretical background object. In that way, distance matrices are of 
    the same size as touch matrices (see generateTouchMatrix). Thus, one 
    can threshold a distance matrix to generate a touch matrix out of it 
    for drawing meshes. 

    Implemented for 2D only at the moment.

    Parameters
    ----------
    coordinate_list1 : Image
    coordinate_list2 : Image
    angle_matrix_destination : Image
    
    Returns
    -------
    angle_matrix_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.generate_distance_matrix(coordinate_list1, coordinate_list2, angle_matrix_destination)
    
    References
    ----------
    """
    from .._tier1 import set
    set(angle_matrix_destination, 0)

    if coordinate_list1.shape[0] > 2:
        raise ValueError('Only 2D pointlists supported!')

    parameters = {
        "dst_matrix": angle_matrix_destination,
        "src_point_list1": coordinate_list1,
        "src_point_list2": coordinate_list2
    }

    execute(__file__, '../clij-opencl-kernels/kernels/generate_angle_matrix_2d_x.cl', 'generate_angle_matrix', angle_matrix_destination.shape, parameters)

    return angle_matrix_destination