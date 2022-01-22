from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import add_images_weighted

@plugin_function(categories=['filter', 'in assistant'], priority=-1)
def large_hessian_eigenvalue(source : Image, destination : Image = None):
    """Determines the Hessian eigenvalues and returns the large eigenvalue image.
    
    Parameters
    ----------
    source : Image
    destination : Image

    Returns
    -------
    destination
    
    """
    from .._tier1 import hessian_eigenvalues
    small, middle, destination = hessian_eigenvalues(source, None, None, destination)
    return destination
