from .._tier0 import execute, create_binary_like
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['binarize', 'in assistant'], output_creator=create_binary_like)
def not_equal_constant(source : Image, destination : Image = None, constant : float = 0):
    """Determines if two images A and B equal pixel wise.
    
    f(a, b) = 1 if a != b; 0 otherwise.Parameters
    ----------
    source : Image
        The image where every pixel is compared to the constant.
    destination : Image
        The resulting binary image where pixels will be 1 only if source1 
    and source2 equal in the given pixel.
    constant : float
        The constant where every pixel is compared to.
     
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.not_equal_constant(source, destination, constant)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_notEqualConstant
    """


    parameters = {
        "src1":source,
        "scalar":float(constant),
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/not_equal_constant_' + str(len(destination.shape)) + 'd_x.cl', 'not_equal_constant_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
