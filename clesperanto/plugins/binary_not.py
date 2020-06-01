from ..core import execute


def binary_not (src1, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src1":src1,
        "dst":dst
    }

    execute(__file__, 'binary_not_' + str(len(dst.shape)) + 'd_x.cl', 'binary_not_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
