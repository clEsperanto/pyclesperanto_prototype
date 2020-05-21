from ..core import execute

def absolute(src, dst):
    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'absolute_' + str(len(dst.shape)) + 'd_x.cl', 'absolute_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
