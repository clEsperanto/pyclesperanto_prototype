from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def replace_intensities(input : Image, new_values_vector : Image, destination : Image = None):
    """Replaces integer intensities specified in a vector image. 
    
    The vector image must be 3D with size (m, 1, 1) where m corresponds to the 
    maximum intensity in the original image. Assuming the vector image 
    contains values (0, 1, 0, 2) means: 
     * All pixels with value 0 (first entry in the vector image) get value 0
     * All pixels with value 1 get value 1
     * All pixels with value 2 get value 0
     * All pixels with value 3 get value 2
     
    
    Parameters
    ----------
    input : Image
    new_values_vector : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.replace_intensities(input, new_values_vector, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_replaceIntensities
    """


    parameters = {
        "dst": destination,
        "src": input,
        "map": new_values_vector
    }

    execute(__file__, '../clij-opencl-kernels/kernels/replace_intensities_x.cl', 'replace_intensities', destination.shape, parameters)
    return destination
