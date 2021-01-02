from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['filter', 'in assistant'], priority=-1)
def exponential(source : Image, destination : Image = None):
    """Computes base exponential of all pixels values.
    
    f(x) = exp(x) 
    
    Author(s): Peter Haub, Robert Haase
    
    Parameters
    ----------
    source : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.exponential(source, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_exponential
    """


    parameters = {
        "src":source,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/exponential_' + str(len(destination.shape)) + 'd_x.cl', 'exponential_' + str(len(destination.shape)) + 'd', destination.shape, parameters)
    return destination
