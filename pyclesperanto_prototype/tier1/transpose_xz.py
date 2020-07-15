from ..tier0 import execute

def transpose_xz (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'transpose_xz_3d_x.cl', 'transpose_xz_3d', dst.shape, parameters)
