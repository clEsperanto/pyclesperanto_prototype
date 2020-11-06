from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

# todo: add a proper output-generator

@plugin_function
def touch_matrix_to_mesh(src_pointlist  : Image, src_touch_matrix : Image, dst_mesh : Image):
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
    mehs_destination : Image
        The output image where results are written into.
         
    Returns
    -------
    mesh_destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.touch_matrix_to_mesh(pointlist, touch_matrix, mesh_destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_touchMatrixToMesh    

    """

    parameters = {
        "src_pointlist": src_pointlist,
        "src_touch_matrix": src_touch_matrix,
        "dst_mesh": dst_mesh
    }

    dimensions = [1, 1, src_touch_matrix.shape[0]]

    execute(__file__, 'touch_matrix_to_mesh_3d_x.cl', 'touch_matrix_to_mesh_3d', dimensions, parameters)

    return dst_mesh
