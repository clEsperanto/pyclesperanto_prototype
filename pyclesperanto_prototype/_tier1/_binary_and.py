from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def binary_and(src1 : Image, src2 : Image, dst : Image = None):
    """Computes a binary image (containing pixel values 0 and 1) from two 
    images X and Y by connecting pairs of
    pixels x and y with the binary AND operator &.
    All pixel values except 0 in the input images are interpreted as 1.
    
    <pre>f(x, y) = x & y</pre>
    
    Parameters
    ----------
    operand1 : Image
        The first binary input image to be processed.
    operand2 : Image
        The second binary input image to be processed.
    destination : Image
        The output image where results are written into.
         
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.binary_and(operand1, operand2, destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_binaryAnd    

    """


    parameters = {
        "src1":src1,
        "src2":src2,
        "dst":dst
    }

    execute(__file__, 'binary_and_' + str(len(dst.shape)) + 'd_x.cl', 'binary_and_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
    return dst
