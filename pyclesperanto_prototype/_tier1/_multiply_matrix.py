from .._tier0 import execute, plugin_function, create_none, create, Image

@plugin_function(output_creator=create_none)
def multiply_matrix(matrix1 : Image, matrix2 : Image, matrix_destination : Image = None):
    """Multiplies two matrices with each other.

    Shape of matrix1 should be equal to shape of matrix2 transposed.
    
    Parameters
    ----------
    matrix1 : Image
    matrix2 : Image
    matrix_destination : Image
    
    Returns
    -------
    matrix_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.multiply_matrix(matrix1, matrix2, matrix_destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_multiplyMatrix
    """
    if matrix_destination is None:
        matrix_destination = create([matrix2.shape[1], matrix1.shape[0]])

    parameters = {
        "dst_matrix":matrix_destination,
        "src1":matrix1,
        "src2":matrix2
    }
    execute(__file__, "../clij-opencl-kernels/kernels/multiply_matrix_x.cl", "multiply_matrix", matrix_destination.shape, parameters)

    return matrix_destination
