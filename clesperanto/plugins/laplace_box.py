from ..core import execute

def laplace_box (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'laplace_box_' + str(len(dst.shape)) + 'd_x.cl', 'laplace_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
