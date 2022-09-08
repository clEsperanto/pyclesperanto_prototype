from pyclesperanto_prototype._tier0 import create_square_matrix_from_labelmap
from pyclesperanto_prototype._tier0 import execute
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image

@plugin_function
def symmetric_maximum_matrix(source_matrix :Image, destination_matrix :Image = None) -> Image:
    """Takes matrix (which might be asymmetric) and makes a symmetrical matrix out of it by taking the maximum value
    of m(x,y) and m(y,x) and storing it in both entries.

    Parameters
    ----------
    source_matrix : Image
    destination_matrix : Image, optional

    Returns
    -------
    destination_matrix
    """
    from .._tier1 import transpose_xy
    from .._tier1 import maximum_images

    temp = transpose_xy(source_matrix)
    destination_matrix = maximum_images(source_matrix, temp, destination_matrix)

    return destination_matrix
