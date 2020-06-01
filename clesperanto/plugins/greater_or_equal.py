from ..core import execute


def greater_or_equal (src1, src2, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src1":src1,
        "src2":src2,
        "dst":dst
    }

    execute(__file__, 'greater_or_equal_' + str(len(dst.shape)) + 'd_x.cl', 'greater_or_equal_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

