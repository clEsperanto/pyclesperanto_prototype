from .._tier0 import sigma_to_kernel_size
from .._tier0 import plugin_function
from .._tier0 import Image
from ._execute_separable_kernel import execute_separable_kernel


@plugin_function
def gaussian_blur(src : Image, dst : Image = None, sigma_x : float = 0, sigma_y : float = 0, sigma_z : float = 0):
    """
    documentation placeholder
    """


    kernel_size_x = sigma_to_kernel_size(sigma_x)
    kernel_size_y = sigma_to_kernel_size(sigma_y)
    kernel_size_z = sigma_to_kernel_size(sigma_z)

    execute_separable_kernel(
        src,
        dst,
        __file__,
        'gaussian_blur_separable_' + str(len(dst.shape)) + 'd_x.cl',
        'gaussian_blur_separable_' + str(len(dst.shape)) + 'd',
        kernel_size_x,
        kernel_size_y,
        kernel_size_z,
        sigma_x,
        sigma_y,
        sigma_z,
        len(dst.shape)
    )

    return dst
