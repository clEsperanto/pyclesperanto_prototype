from .._tier0 import radius_to_kernel_size
from ._execute_separable_kernel import execute_separable_kernel
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def minimum_box(src : Image, dst : Image = None, radius_x : float = 0, radius_y : float = 0, radius_z : float = 0):
    """Computes the local minimum of a pixels cube neighborhood. 
    
    The cubes size is specified by 
    its half-width, half-height and half-depth (radius). 

    Parameters
    ----------
    source : Image
    destination : Image
    radiusX : Number
    radiusY : Number
    radiusZ : Number
    
    
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.minimum_box(source, destination, radiusX, radiusY, radiusZ)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_minimum3DBox    

    """


    kernel_size_x = radius_to_kernel_size(radius_x)
    kernel_size_y = radius_to_kernel_size(radius_y)
    kernel_size_z = radius_to_kernel_size(radius_z)

    execute_separable_kernel(
        src,
        dst,
        __file__,
        'minimum_separable_' + str(len(dst.shape)) + 'd_x.cl',
        'minimum_separable_' + str(len(dst.shape)) + 'd',
        kernel_size_x,
        kernel_size_y,
        kernel_size_z,
        radius_x,
        radius_y,
        radius_z,
        len(dst.shape)
    )
    return dst
