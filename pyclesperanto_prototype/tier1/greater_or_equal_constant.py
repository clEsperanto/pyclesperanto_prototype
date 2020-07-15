from ..tier0 import execute


def greater_or_equal_constant (src1, dst, scalar):
    """Determines if two images A and B greater or equal pixel wise. 
    
    f(a, b) = 1 if a >= b; 0 otherwise. 

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number constant)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_greaterOrEqualConstant


    Returns
    -------

    """


    parameters = {
        "src1":src1,
        "scalar":float(scalar),
        "dst":dst
    }

    execute(__file__, 'greater_or_equal_constant_' + str(len(dst.shape)) + 'd_x.cl', 'greater_or_equal_constant_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

