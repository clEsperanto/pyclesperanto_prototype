from .._tier0 import sigma_to_kernel_size
from .._tier0 import plugin_function
from .._tier0 import Image
from ._execute_separable_kernel import execute_separable_kernel

@plugin_function(categories=['filter', 'denoise', 'in assistant'], priority=1)
def gaussian_blur(source : Image, destination : Image = None, sigma_x : float = 0, sigma_y : float = 0, sigma_z : float = 0):
    """Computes the Gaussian blurred image of an image given sigma values
    in X, Y and Z. 
    
    Thus, the filter kernel can have non-isotropic shape.
    
    The implementation is done separable. In case a sigma equals zero, the 
    direction is not blurred. 
    
    Parameters
    ----------
    source : Image
    destination : Image
    sigma_x : Number
    sigma_y : Number
    sigma_z : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.gaussian_blur(source, destination, sigma_x, sigma_y, sigma_z)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_gaussianBlur3D
    """


    kernel_size_x = sigma_to_kernel_size(sigma_x)
    kernel_size_y = sigma_to_kernel_size(sigma_y)
    kernel_size_z = sigma_to_kernel_size(sigma_z)

    execute_separable_kernel(
        source,
        destination,
        __file__,
        '../clij-opencl-kernels/kernels/gaussian_blur_separable_' + str(len(destination.shape)) + 'd_x.cl',
        'gaussian_blur_separable_' + str(len(destination.shape)) + 'd',
        kernel_size_x,
        kernel_size_y,
        kernel_size_z,
        sigma_x,
        sigma_y,
        sigma_z,
        len(destination.shape)
    )

    return destination
