from .._tier0 import Image
from .._tier0 import plugin_function

@plugin_function
def is_matrix_symmetric(matrix: Image) -> bool:
    """Tests if a matrix is symmetric and returns the result of the test as boolean
    """
    from .._tier1 import transpose_xy
    from .._tier4 import mean_squared_error
    if matrix.shape[-2] != matrix.shape[-1]:
        return False

    matrix_transposed = transpose_xy(matrix)
    return mean_squared_error(matrix, matrix_transposed) == 0
