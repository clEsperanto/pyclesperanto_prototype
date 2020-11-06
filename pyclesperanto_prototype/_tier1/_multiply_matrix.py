from .._tier0 import execute


def multiply_matrix(input1, input2, output):
    """Multiplies two matrices with each other. 

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
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_multiplyMatrix    

    """


    parameters = {
        "dst_matrix":output,
        "src1":input1,
        "src2":input2
    };
    execute(__file__, "multiply_matrix_x.cl", "multiply_matrix", output.shape, parameters);


