from ..core import execute


def exponential (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'exponential_' + str(len(dst.shape)) + 'd_x.cl', 'exponential_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

