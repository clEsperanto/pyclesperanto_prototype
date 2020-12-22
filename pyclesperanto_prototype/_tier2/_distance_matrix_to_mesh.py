from pyclesperanto_prototype._tier0 import execute
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import create_from_pointlist

@plugin_function(output_creator=create_from_pointlist)
def distance_matrix_to_mesh(pointlist : Image, distance_matrix : Image, mesh_destination : Image, maximum_distance : float = 1):
    """Generates a mesh from a distance matric and a list of point coordinates.
    
    Takes a pointlist with dimensions n*d with n point coordinates in d 
    dimensions and a distance matrix of size n*n to draw lines from all 
    points to points if the corresponding pixel in the distance matrix is 
    smaller than a given distance threshold. 
    
    Parameters
    ----------
    pointlist : Image
    distance_matrix : Image
    mesh_destination : Image
    maximum_distance : Number
    
    Returns
    -------
    mesh_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_distanceMatrixToMesh
    """
    from .._tier1 import smaller_or_equal_constant
    from .._tier1 import touch_matrix_to_mesh

    touch_matrix = smaller_or_equal_constant(distance_matrix, constant=maximum_distance)
    mesh_destination = touch_matrix_to_mesh(pointlist, touch_matrix, mesh_destination)

    return mesh_destination
