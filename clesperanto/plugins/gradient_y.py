from ..core import execute

def gradient_y (src, dst):

    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'gradient_y_' + str(len(dst.shape)) + 'd_x.cl', 'gradient_y_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
