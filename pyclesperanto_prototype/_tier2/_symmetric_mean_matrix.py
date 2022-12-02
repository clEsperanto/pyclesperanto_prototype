from pyclesperanto_prototype._tier0 import create_square_matrix_from_labelmap
from pyclesperanto_prototype._tier0 import execute
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image

@plugin_function
def symmetric_mean_matrix(source_matrix :Image, destination_matrix :Image = None) -> Image:
    """Takes matrix (which might be asymmetric) and makes a symmetrical matrix out of it by taking the mean value
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
    from .._tier1 import add_images_weighted

    temp = transpose_xy(source_matrix)
    destination_matrix = add_images_weighted(source_matrix, temp, destination_matrix, 0.5, 0.5)

    return destination_matrix
