from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'binary processing', 'in assistant', 'combine labels', 'label processing'], output_creator=create_binary_like)
def binary_or(operand1 : Image, operand2 : Image, destination : Image = None) -> Image:
    """Computes a binary image (containing pixel values 0 and 1) from two 
    images X and Y by connecting pairs of
    pixels x and y with the binary OR operator |.
    
    All pixel values except 0 in the input images are interpreted as 
    1.<pre>f(x, y) = x | y</pre>
    
    Parameters
    ----------
    operand1 : Image
        The first binary input image to be processed.
    operand2 : Image
        The second binary input image to be processed.
    destination : Image, optional
        The output image where results are written into.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.binary_or(operand1, operand2, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_binaryOr
    """


    parameters = {
        "src1":operand1,
        "src2":operand2,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/binary_or_' + str(len(destination.shape)) + 'd_x.cl', 'binary_or_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
