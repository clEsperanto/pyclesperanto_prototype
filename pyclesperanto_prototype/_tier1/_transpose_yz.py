from .._tier0 import execute

def transpose_yz (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'transpose_yz_3d_x.cl', 'transpose_yz_3d', dst.shape, parameters)
