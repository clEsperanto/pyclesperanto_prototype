from typing import Union

from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push
from ._AffineTransform3D import AffineTransform3D
from skimage.transform import AffineTransform
import numpy as np

@plugin_function
def affine_transform(source : Image, destination : Image = None, transform : Union[np.ndarray, AffineTransform3D, AffineTransform] = None, linear_interpolation : bool = False):
    """
    Applies an affine transform to an image.

    Parameters
    ----------
    source : Image
        image to be transformed
    destination : Image, optional
        image where the transformed image should be written to
    transform : 4x4 numpy array or AffineTransform3D object or skimage.transform.AffineTransform object
        transform matrix or object describing the transformation
    linear_interpolation: bool
        If true, bi-/tri-linear interplation will be applied.
        If false, nearest-neighbor interpolation wille be applied.

    Returns
    -------
    destination

    """
    import numpy as np
    from .._tier0 import empty_image_like
    from .._tier0 import execute
    from .._tier1 import copy
    from .._tier0 import create
    from .._tier1 import copy_slice

    # deal with 2D input images
    if len(source.shape) == 2:
        source_3d = create([1, source.shape[0], source.shape[1]])
        copy_slice(source, source_3d, 0)
        source = source_3d

    # deal with 2D output images
    original_destination = destination
    copy_back_after_transforming = False
    if len(destination.shape) == 2:
        destination = create([1, destination.shape[0], destination.shape[1]])
        copy_slice(original_destination, destination, 0)
        copy_back_after_transforming = True

        # we invert the transform because we go from the target image to the source image to read pixels
    if isinstance(transform, AffineTransform3D):
        transform_matrix = np.asarray(transform.copy().inverse())
    elif isinstance(transform, AffineTransform):
        matrix = np.asarray(transform.params)
        matrix = np.asarray([
            [matrix[0,0], matrix[0,1], 0, matrix[0,2]],
            [matrix[1,0], matrix[1,1], 0, matrix[1,2]],
            [0, 0, 1, 0],
            [matrix[2,0], matrix[2,1], 0, matrix[2,2]]
        ])
        transform_matrix = np.linalg.inv(matrix)
    else:
        transform_matrix = np.linalg.inv(transform)

    gpu_transform_matrix = push(transform_matrix)

    kernel_suffix = ''
    if linear_interpolation:
        image = empty_image_like(source)
        copy(source, image)
        if type(source) != type(image):
            kernel_suffix = '_interpolate'
        source = image


    parameters = {
        "input": source,
        "output": destination,
        "mat": gpu_transform_matrix
    }

    execute(__file__, '../clij-opencl-kernels/kernels/affine_transform_' + str(len(destination.shape)) + 'd' + kernel_suffix + '_x.cl',
            'affine_transform_' + str(len(destination.shape)) + 'd' + kernel_suffix, destination.shape, parameters)

    # deal with 2D output images
    if copy_back_after_transforming:
        copy_slice(destination, original_destination, 0)

    return original_destination