from ..tier0 import execute

def transpose_xy (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'transpose_xy_3d_x.cl', 'transpose_xy_3d', dst.shape, parameters)
