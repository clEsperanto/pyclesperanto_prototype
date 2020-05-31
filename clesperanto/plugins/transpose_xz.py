from ..core import execute

def transpose_xz (src, dst):

    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'transpose_xz_3d_x.cl', 'transpose_xz_3d', dst.shape, parameters)
