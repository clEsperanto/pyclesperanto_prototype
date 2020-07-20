from .._tier0 import execute


def multiply_matrix(input1, input2, output):
    """Multiplies two matrices with each other.

    Available for: 2D

    Parameters
    ----------
    (Image matrix1, Image matrix2, ByRef Image matrix_destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_multiplyMatrix


    Returns
    -------

    """


    parameters = {
        "dst_matrix":output,
        "src1":input1,
        "src2":input2
    };
    execute(__file__, "multiply_matrix_x.cl", "multiply_matrix", output.shape, parameters);


