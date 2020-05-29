from ..core import execute

def laplace_diamond (src, dst):

    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'laplace_diamond_' + str(len(dst.shape)) + 'd_x.cl', 'laplace_diamond_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
