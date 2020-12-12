from pyclesperanto_prototype._tier0 import execute
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import create_from_pointlist

@plugin_function(output_creator=create_from_pointlist)
def distance_matrix_to_mesh(pointlist : Image, distance_matrix : Image, mesh_destination : Image, distance_threshold : float = 1):
    """

    Parameters
    ----------
    pointlist
    touch_matrix
    mesh_destination

    Returns
    -------

    """
    from .._tier1 import smaller_or_equal_constant
    from .._tier1 import touch_matrix_to_mesh

    touch_matrix = smaller_or_equal_constant(distance_matrix, constant=distance_threshold)
    mesh_destination = touch_matrix_to_mesh(pointlist, touch_matrix, mesh_destination)

    return mesh_destination
