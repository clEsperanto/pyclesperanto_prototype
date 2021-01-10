from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push_zyx
from ._AffineTransform3D import AffineTransform3D

@plugin_function
def affine_transform(source : Image, destination : Image, transform : AffineTransform3D, linear_interpolation : bool = False):
    """
    Applies an affine transform to an image.

    Parameters
    ----------
    source
    destination
    transform
    linear_interpolation

    Returns
    -------

    """
    import numpy as np
    from .._tier0 import empty_image_like
    from .._tier0 import execute
    from .._tier1 import copy

    transform_matrix = np.asarray(transform.copy().inverse())

    gpu_transform_matrix = push_zyx(transform_matrix)

    kernel_suffix = ''
    if linear_interpolation:
        image = empty_image_like(source)
        copy(source, image)
        source = image
        kernel_suffix = '_interpolate'


    parameters = {
        "input": source,
        "output": destination,
        "mat": gpu_transform_matrix
    }

    execute(__file__, '../clij-opencl-kernels/kernels/affine_transform_' + str(len(destination.shape)) + 'd' + kernel_suffix + '_x.cl',
            'affine_transform_' + str(len(destination.shape)) + 'd' + kernel_suffix, destination.shape, parameters)


    return destination