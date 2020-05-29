from ..core import radius_to_kernel_size
from .execute_separable_kernel import execute_separable_kernel

def maximum_box (src, dst, radius_x, radius_y, radius_z):
    kernel_size_x = radius_to_kernel_size(radius_x)
    kernel_size_y = radius_to_kernel_size(radius_y)
    kernel_size_z = radius_to_kernel_size(radius_z)

    execute_separable_kernel(
        src,
        dst,
        __file__,
        'maximum_separable_' + str(len(dst.shape)) + 'd_x.cl',
        'maximum_separable_' + str(len(dst.shape)) + 'd',
        kernel_size_x,
        kernel_size_y,
        kernel_size_z,
        radius_x,
        radius_y,
        radius_z,
        len(dst.shape)
    )
