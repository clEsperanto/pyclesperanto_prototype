from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_from_pointlist

@plugin_function(output_creator=create_from_pointlist)
def touch_matrix_to_mesh(pointlist  : Image, touch_matrix : Image, mesh_destination : Image):
    """Takes a pointlist with dimensions n*d with n point coordinates in d 
    dimensions and a touch matrix of 
    size n*n to draw lines from all points to points if the corresponding pixel 
    in the touch matrix is 1.
    
    Parameters
    ----------
    pointlist : Image
        n*d matrix representing n coordinates with d dimensions.
    touch_matrix : Image
        A 2D binary matrix with 1 in pixels (i,j) where label i touches 
    label j.
    mesh_destination : Image
        The output image where results are written into.
     
    
    Returns
    -------
    mesh_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.touch_matrix_to_mesh(pointlist, touch_matrix, mesh_destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_touchMatrixToMesh
    """

    parameters = {
        "src_pointlist": pointlist,
        "src_touch_matrix": touch_matrix,
        "dst_mesh": mesh_destination
    }

    dimensions = [1, 1, touch_matrix.shape[0]]
    from .._tier1 import set
    set(mesh_destination, 0)
    execute(__file__, '../clij-opencl-kernels/kernels/touch_matrix_to_mesh_3d_x.cl', 'touch_matrix_to_mesh_3d', dimensions, parameters)

    return mesh_destination
