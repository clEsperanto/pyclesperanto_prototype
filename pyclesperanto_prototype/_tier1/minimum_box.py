from .._tier0 import radius_to_kernel_size
from .execute_separable_kernel import execute_separable_kernel

def minimum_box (src, dst, radius_x, radius_y, radius_z):
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
