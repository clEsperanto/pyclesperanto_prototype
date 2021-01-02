from .._tier0 import radius_to_kernel_size
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def multiply_image_and_coordinate(source : Image, destination : Image = None, dimension = 0):
    """Multiplies all pixel intensities with the x, y or z coordinate, 
    depending on specified dimension. 
    
    Parameters
    ----------
    source : Image
    destination : Image
    dimension : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.multiply_image_and_coordinate(source, destination, dimension)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_multiplyImageAndCoordinate
    """

    parameters = {
        "src":source,
        "dst":destination,
        "dimension":int(dimension)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/multiply_image_and_coordinate_' + str(len(destination.shape)) + 'd_x.cl', 'multiply_image_and_coordinate_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
