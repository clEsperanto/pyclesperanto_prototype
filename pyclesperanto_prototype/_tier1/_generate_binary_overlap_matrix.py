from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_square_matrix_from_two_labelmaps
from .._tier0 import execute

@plugin_function(output_creator=create_square_matrix_from_two_labelmaps)
def generate_binary_overlap_matrix(label_map1 : Image, label_map2 : Image, binary_overlap_matrix : Image = None):
    """
    
    Parameters
    ----------
    label_map1
    label_map2

    Returns
    -------

    """
    from .._tier1 import set

    set(binary_overlap_matrix, 0)

    parameters = {
        "dst_matrix":binary_overlap_matrix,
        "src_label_map1":label_map1,
        "src_label_map2":label_map2
    }

    execute(__file__, 'generate_binary_overlap_matrix_' + str(len(label_map1.shape)) + 'd_x.cl', 'generate_binary_overlap_matrix_' + str(len(label_map1.shape)) + 'd', label_map1.shape, parameters)
    return binary_overlap_matrix