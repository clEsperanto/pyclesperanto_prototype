from .._tier0 import create_square_matrix_from_labelmap
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_square_matrix_from_labelmap)
def generate_touch_matrix(labelmap :Image, touch_matrix_output :Image = None):
    from .._tier1 import set
    """
    docs
    """
    set(touch_matrix_output, 0)

    parameters = {
        "dst_matrix": touch_matrix_output,
        "src_label_map": labelmap
    }

    execute(__file__, 'generate_touch_matrix_' + str(len(labelmap.shape)) + 'd_x.cl', 'generate_touch_matrix_' + str(len(labelmap.shape)) + 'd', labelmap.shape, parameters)

    return touch_matrix_output