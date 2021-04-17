from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['combine', 'binarize', 'in assistant'], output_creator=create_binary_like)
def equal(source1 : Image, source2 : Image, destination : Image = None):
    """Determines if two images A and B equal pixel wise.
    
    <pre>f(a, b) = 1 if a == b; 0 otherwise.</pre>
    
    Parameters
    ----------
    source1 : Image
        The first image to be compared with.
    source2 : Image
        The second image to be compared with the first.
    destination : Image
        The resulting binary image where pixels will be 1 only if source1 
    and source2 equal in the given pixel.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.equal(source1, source2, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_equal
    """


    parameters = {
        "src1":source1,
        "src2":source2,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/equal_' + str(len(destination.shape)) + 'd_x.cl', 'equal_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
