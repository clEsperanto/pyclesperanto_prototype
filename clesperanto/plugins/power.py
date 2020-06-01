from ..core import execute


def power (src, dst, exponent):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst": dst,
        "exponent":float(exponent)
    }

    execute(__file__, 'power_' + str(len(dst.shape)) + 'd_x.cl', 'power_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

