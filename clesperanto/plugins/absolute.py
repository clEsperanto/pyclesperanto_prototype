from ..core import execute

def absolute(src, dst):
    parameters = {
        "src":src,
        "dst":dst
    }
    if (len(dst.shape) == 2):
        execute(__file__, 'absolute_2d_x.cl', 'absolute_2d', dst.shape, parameters)
    else:
        execute(__file__, 'absolute_3d_x.cl', 'absolute_3d', dst.shape, parameters)
