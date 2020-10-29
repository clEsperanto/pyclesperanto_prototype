from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

# todo: add a proper output-generator

@plugin_function
def touch_matrix_to_mesh(src_pointlist  : Image, src_touch_matrix : Image, dst_mesh : Image):
    """
    docs
    """

    parameters = {
        "src_pointlist": src_pointlist,
        "src_touch_matrix": src_touch_matrix,
        "dst_mesh": dst_mesh
    }

    dimensions = [1, 1, src_touch_matrix.shape[0]]

    execute(__file__, 'touch_matrix_to_mesh_3d_x.cl', 'touch_matrix_to_mesh_3d', dimensions, parameters)

    return dst_mesh
