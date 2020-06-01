from ..core import execute


def multiply_matrix(input1, input2, output):
    """
    documentation placeholder
    """


    parameters = {
        "dst_matrix":output,
        "src1":input1,
        "src2":input2
    };
    execute(__file__, "multiply_matrix_x.cl", "multiply_matrix", output.shape, parameters);


