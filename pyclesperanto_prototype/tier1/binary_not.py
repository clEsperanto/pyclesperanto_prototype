from ..tier0 import execute


def binary_not (src1, dst):
    """Computes a binary image (containing pixel values 0 and 1) from an image X by negating its pixel values
    x using the binary NOT operator !
    
    All pixel values except 0 in the input image are interpreted as 1.
    
    <pre>f(x) = !x</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_binaryNot


    Returns
    -------

    """


    parameters = {
        "src1":src1,
        "dst":dst
    }

    execute(__file__, 'binary_not_' + str(len(dst.shape)) + 'd_x.cl', 'binary_not_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
