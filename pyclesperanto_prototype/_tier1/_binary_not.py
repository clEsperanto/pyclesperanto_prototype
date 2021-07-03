from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['binary processing', 'filter', 'label processing', 'in assistant'], output_creator=create_binary_like)
def binary_not(source : Image, destination : Image = None):
    """Computes a binary image (containing pixel values 0 and 1) from an image 
    X by negating its pixel values
    x using the binary NOT operator !
    
    All pixel values except 0 in the input image are interpreted as 1.
    
    <pre>f(x) = !x</pre>
    
    Parameters
    ----------
    source : Image
        The binary input image to be inverted.
    destination : Image
        The output image where results are written into.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.binary_not(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_binaryNot
    """


    parameters = {
        "src1":source,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/binary_not_' + str(len(destination.shape)) + 'd_x.cl', 'binary_not_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
