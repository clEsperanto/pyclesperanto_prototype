from ..core import execute


def logarithm (src, dst):

    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'logarithm_' + str(len(dst.shape)) + 'd_x.cl', 'logarithm_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

