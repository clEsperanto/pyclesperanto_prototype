from ..core import execute


def equal (src1, src2, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src1":src1,
        "src2":src2,
        "dst":dst
    }

    execute(__file__, 'equal_' + str(len(dst.shape)) + 'd_x.cl', 'equal_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

