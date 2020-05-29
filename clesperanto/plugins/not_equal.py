from ..core import execute


def not_equal (src1, src2, dst):

    parameters = {
        "src1":src1,
        "src2":src2,
        "dst":dst
    }

    execute(__file__, 'not_equal_' + str(len(dst.shape)) + 'd_x.cl', 'not_equal_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

