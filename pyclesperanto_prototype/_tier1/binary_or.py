from .._tier0 import execute

def binary_or (src1, src2, dst):
    """Computes a binary image (containing pixel values 0 and 1) from two images X and Y by connecting pairs of
    pixels x and y with the binary OR operator |.
    
    All pixel values except 0 in the input images are interpreted as 1.<pre>f(x, y) = x | y</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image operand1, Image operand2, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_binaryOr


    Returns
    -------

    """


    parameters = {
        "src1":src1,
        "src2":src2,
        "dst":dst
    }

    execute(__file__, 'binary_or_' + str(len(dst.shape)) + 'd_x.cl', 'binary_or_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
