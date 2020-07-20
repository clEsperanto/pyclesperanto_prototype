from .._tier0 import execute

# todo: add a proper output-generator

def touch_matrix_to_mesh (src_pointlist, src_touch_matrix, dst_mesh):
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