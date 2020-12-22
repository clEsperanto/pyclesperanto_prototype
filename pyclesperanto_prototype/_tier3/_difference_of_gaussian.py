from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier1 import gaussian_blur
from pyclesperanto_prototype._tier0 import create_like
from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier2 import subtract_images

@plugin_function(categories=['filter', 'background removal'])
def difference_of_gaussian(input : Image, destination : Image = None, sigma1_x : float = 2, sigma1_y : float = 2, sigma1_z : float = 2, sigma2_x : float = 2, sigma2_y : float = 2, sigma2_z : float = 2):
    """Applies Gaussian blur to the input image twice with different sigma 
    values resulting in two images which are then subtracted from each other.
    
    It is recommended to apply this operation to images of type Float (32 bit) 
    as results might be negative.
    
    Parameters
    ----------
    input : Image
        The input image to be processed.
    destination : Image
        The output image where results are written into.
    sigma1_x : float
        Sigma of the first Gaussian filter in x
    sigma1_y : float
        Sigma of the first Gaussian filter in y
    sigma1_z : float
        Sigma of the first Gaussian filter in z
    sigma2_x : float
        Sigma of the second Gaussian filter in x
    sigma2_y : float
        Sigma of the second Gaussian filter in y
    sigma2_z : float
        Sigma of the second Gaussian filter in z 
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.difference_of_gaussian(input, destination, sigma1x, sigma1y, sigma1z, sigma2x, sigma2y, sigma2z)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_differenceOfGaussian3D
    """
    temp1 = create_like(destination)
    temp2 = create_like(destination)

    gaussian_blur(input, temp1, sigma1_x, sigma1_y, sigma1_z)
    gaussian_blur(input, temp2, sigma2_x, sigma2_y, sigma2_z)

    return subtract_images(temp1, temp2, destination)

