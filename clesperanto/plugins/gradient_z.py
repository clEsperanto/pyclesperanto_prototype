from ..core import execute

def gradient_z (src, dst):

    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'gradient_z_3d_x.cl', 'gradient_z_3d', dst.shape, parameters)
