from .._tier0 import radius_to_kernel_size
from ._execute_separable_kernel import execute_separable_kernel
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def mean_box(src : Image, dst : Image = None, radius_x : float = 1, radius_y : float = 1, radius_z : float = 1):
    """
    documentation placeholder
    """


    kernel_size_x = radius_to_kernel_size(radius_x)
    kernel_size_y = radius_to_kernel_size(radius_y)
    kernel_size_z = radius_to_kernel_size(radius_z)

    execute_separable_kernel(
        src,
        dst,
        __file__,
        'mean_separable_' + str(len(dst.shape)) + 'd_x.cl',
        'mean_separable_' + str(len(dst.shape)) + 'd',
        kernel_size_x,
        kernel_size_y,
        kernel_size_z,
        radius_x,
        radius_y,
        radius_z,
        len(dst.shape)
    )
    return dst
