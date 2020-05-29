from ..core import execute


def greater_constant (src1, dst, scalar):

    parameters = {
        "src1":src1,
        "scalar":float(scalar),
        "dst":dst
    }

    execute(__file__, 'greater_constant_' + str(len(dst.shape)) + 'd_x.cl', 'greater_constant_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

