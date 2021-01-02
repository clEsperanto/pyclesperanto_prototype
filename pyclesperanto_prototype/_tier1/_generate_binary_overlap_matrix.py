from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_square_matrix_from_two_labelmaps
from .._tier0 import execute

@plugin_function(output_creator=create_square_matrix_from_two_labelmaps)
def generate_binary_overlap_matrix(label_map1 : Image, label_map2 : Image, binary_overlap_matrix_destination : Image = None):
    """Takes two labelmaps with n and m labels and generates a (n+1)*(m+1) 
    matrix where all pixels are set to 0 exept those where labels overlap 
    between the label maps. 
    
    For example, if labels 3 in labelmap1 and 4 in labelmap2 are touching then 
    the pixel (3,4) in the matrix will be set to 1. 
    
    Parameters
    ----------
    label_map1 : Image
    label_map2 : Image
    binary_overlap_matrix_destination : Image
    
    Returns
    -------
    binary_overlap_matrix_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_generateBinaryOverlapMatrix
    """
    from .._tier1 import set

    set(binary_overlap_matrix_destination, 0)

    parameters = {
        "dst_matrix":binary_overlap_matrix_destination,
        "src_label_map1":label_map1,
        "src_label_map2":label_map2
    }

    execute(__file__, '../clij-opencl-kernels/kernels/generate_binary_overlap_matrix_' + str(len(label_map1.shape)) + 'd_x.cl', 'generate_binary_overlap_matrix_' + str(len(label_map1.shape)) + 'd', label_map1.shape, parameters)
    return binary_overlap_matrix_destination