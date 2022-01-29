from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import add_images_weighted

@plugin_function(categories=['filter', 'in assistant'], priority=-1)
def small_hessian_eigenvalue(source : Image, destination : Image = None) -> Image:
    """Determines the Hessian eigenvalues and returns the small eigenvalue image.
    
    Parameters
    ----------
    source : Image
    destination : Image

    Returns
    -------
    destination
    
    """
    from .._tier1 import hessian_eigenvalues
    destination, middle, large = hessian_eigenvalues(source, destination)
    return destination
