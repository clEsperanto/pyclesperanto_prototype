from ..core import execute


def smaller_or_equal_constant (src1, dst, scalar):

    parameters = {
        "src1":src1,
        "scalar":float(scalar),
        "dst":dst
    }

    execute(__file__, 'smaller_or_equal_constant_' + str(len(dst.shape)) + 'd_x.cl', 'smaller_or_equal_constant_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

