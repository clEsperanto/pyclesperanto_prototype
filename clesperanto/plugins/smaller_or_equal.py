from ..core import execute


def smaller_or_equal (src1, src2, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src1":src1,
        "src2":src2,
        "dst":dst
    }

    execute(__file__, 'smaller_or_equal_' + str(len(dst.shape)) + 'd_x.cl', 'smaller_or_equal_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

