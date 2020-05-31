from ..core import execute

def sobel (src, dst):

    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'sobel_' + str(len(dst.shape)) + 'd_x.cl', 'sobel_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
