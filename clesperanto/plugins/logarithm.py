from ..core import execute


def logarithm (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'logarithm_' + str(len(dst.shape)) + 'd_x.cl', 'logarithm_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

