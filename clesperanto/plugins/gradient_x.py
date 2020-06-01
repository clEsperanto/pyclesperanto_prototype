from ..core import execute

def gradient_x (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'gradient_x_' + str(len(dst.shape)) + 'd_x.cl', 'gradient_x_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
