from ..core import execute


def greater_constant (src1, dst, scalar):
    """Determines if two images A and B greater pixel wise. 
    
    f(a, b) = 1 if a > b; 0 otherwise. 

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number constant)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_greaterConstant


    Returns
    -------

    """


    parameters = {
        "src1":src1,
        "scalar":float(scalar),
        "dst":dst
    }

    execute(__file__, 'greater_constant_' + str(len(dst.shape)) + 'd_x.cl', 'greater_constant_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

