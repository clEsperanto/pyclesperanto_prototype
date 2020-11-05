from .._tier0 import execute

def binary_subtract (src1, src2, dst):
    """Subtracts one binary image from another.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image minuend, Image subtrahend, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_binarySubtract


    Returns
    -------

    """


    parameters = {
        "dst": dst,
        "src1":src1,
        "src2":src2
    }

    execute(__file__, 'binary_subtract_' + str(len(dst.shape)) + 'd_x.cl', 'binary_subtract_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
