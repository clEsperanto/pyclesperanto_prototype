from .._tier0 import execute


def smaller_or_equal_constant (src1, dst, scalar):
    """Determines if two images A and B smaller or equal pixel wise.
    
    f(a, b) = 1 if a <= b; 0 otherwise. 

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number constant)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_smallerOrEqualConstant


    Returns
    -------

    """


    parameters = {
        "src1":src1,
        "scalar":float(scalar),
        "dst":dst
    }

    execute(__file__, 'smaller_or_equal_constant_' + str(len(dst.shape)) + 'd_x.cl', 'smaller_or_equal_constant_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

