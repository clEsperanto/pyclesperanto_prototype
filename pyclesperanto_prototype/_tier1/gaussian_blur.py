from .._tier0 import sigma_to_kernel_size
from .execute_separable_kernel import execute_separable_kernel

def gaussian_blur (src, dst, sigma_x, sigma_y, sigma_z):
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
