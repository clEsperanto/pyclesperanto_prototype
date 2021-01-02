from .._tier0 import create_square_matrix_from_labelmap
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_square_matrix_from_labelmap)
def generate_touch_matrix(label_map :Image, touch_matrix_destination :Image = None):
    from .._tier1 import set
    """Takes a labelmap with n labels and generates a (n+1)*(n+1) matrix where 
    all pixels are set to 0 exept those where labels are touching. 
    
    Only half of the matrix is filled (with x < y). For example, if labels 3 and 
    4 are touching then the pixel (3,4) in the matrix will be set to 1.
    The touch matrix is a representation of a region adjacency graph
     
    
    Parameters
    ----------
    label_map : Image
    touch_matrix_destination : Image
    
    Returns
    -------
    touch_matrix_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.generate_touch_matrix(label_map, touch_matrix_destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_generateTouchMatrix
    """
    set(touch_matrix_destination, 0)

    parameters = {
        "dst_matrix": touch_matrix_destination,
        "src_label_map": label_map
    }

    execute(__file__, '../clij-opencl-kernels/kernels/generate_touch_matrix_' + str(len(label_map.shape)) + 'd_x.cl', 'generate_touch_matrix_' + str(len(label_map.shape)) + 'd', label_map.shape, parameters)

    return touch_matrix_destination