from .._tier0 import execute

def detect_maxima_box (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    # todo: ensure detect_maxima_2d_x.cl fit to naming convention
    execute(__file__, 'detect_maxima_' + str(len(dst.shape)) + 'd_x.cl', 'detect_maxima_' + str(len(dst.shape)) + 'd', dst.shape, parameters)


