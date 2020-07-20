from .._tier0 import create_matrix_from_pointlists
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_matrix_from_pointlists)
def generate_distance_matrix(pointlist1 :Image, pointlist2 :Image, distance_matrix_output :Image = None):
    from .._tier1 import set
    """
    docs
    """
    set(distance_matrix_output, 0)

    parameters = {
        "dst_matrix": distance_matrix_output,
        "src_point_list1": pointlist1,
        "src_point_list2": pointlist2
    }

    execute(__file__, 'generate_distance_matrix_x.cl', 'generate_distance_matrix', distance_matrix_output.shape, parameters)

    return distance_matrix_output