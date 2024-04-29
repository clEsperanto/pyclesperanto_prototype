from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'binary processing', 'in assistant', 'combine labels', 'label processing'], output_creator=create_binary_like)
def binary_subtract(minuend : Image, subtrahend : Image, destination : Image = None) -> Image:
    """Subtracts one binary image from another.
    
    Parameters
    ----------
    minuend : Image
        The first binary input image to be processed.
    subtrahend : Image
        The second binary input image to be subtracted from the first.
    destination : Image, optional
        The output image where results are written into.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.binary_subtract(minuend, subtrahend, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_binarySubtract
    """


    parameters = {
        "dst": destination,
        "src1":minuend,
        "src2":subtrahend
    }
    execute(__file__, '../clij-opencl-kernels/kernels/binary_subtract_' + str(len(destination.shape)) + 'd_x.cl', 'binary_subtract_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
