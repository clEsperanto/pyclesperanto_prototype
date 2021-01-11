from typing import Union

from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push
from ._AffineTransform3D import AffineTransform3D
from skimage.transform import AffineTransform
import numpy as np

@plugin_function
def affine_transform(source : Image, output : Image = None, transform : Union[np.ndarray, AffineTransform3D, AffineTransform] = None, linear_interpolation : bool = False, matrix : np.ndarray = None):
    """
    Applies an affine transform to an image.

    Parameters
    ----------
    source : Image
        image to be transformed
    output : Image, optional
        image where the transformed image should be written to
    transform : 4x4 numpy array or AffineTransform3D object or skimage.transform.AffineTransform object
        transform matrix or object describing the transformation. Internally, this transform is inverted.
    linear_interpolation: bool
        not implemented yet
    matrix : 4x4 numpy array
        affine transform matrix, overwrites parameter transform if set

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
    original_destination = output
    copy_back_after_transforming = False
    if len(output.shape) == 2:
        output = create([1, output.shape[0], output.shape[1]])
        copy_slice(original_destination, output, 0)
        copy_back_after_transforming = True

    if matrix is None:
        # we invert the transform because we go from the target image to the source image to read pixels
        if isinstance(transform, AffineTransform3D):
            transform_matrix = np.asarray(transform.copy().inverse())
        elif isinstance(transform, AffineTransform):
            transform = np.asarray(transform.params)
            transform = np.asarray([
                [transform[0,0], transform[0,1], 0, transform[0,2]],
                [transform[1,0], transform[1,1], 0, transform[1,2]],
                [0, 0, 1, 0],
                [transform[2,0], transform[2,1], 0, transform[2,2]]
            ])
            transform_matrix = np.linalg.inv(transform)
        else:
            transform_matrix = np.linalg.inv(transform)
    else:
        # transpose X and Z to make matrix be compatible to scipy
        transpose_matrix = np.asarray([
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 1]
        ])
        matrix = np.matmul(transpose_matrix, matrix)
        matrix = np.matmul(matrix, transpose_matrix)
        transform_matrix = matrix

    gpu_transform_matrix = push(transform_matrix)

    kernel_suffix = ''
    if linear_interpolation:
        image = empty_image_like(source)
        copy(source, image)
        source = image
        kernel_suffix = '_interpolate'


    parameters = {
        "input": source,
        "output": output,
        "mat": gpu_transform_matrix
    }

    execute(__file__, '../clij-opencl-kernels/kernels/affine_transform_' + str(len(output.shape)) + 'd' + kernel_suffix + '_x.cl',
            'affine_transform_' + str(len(output.shape)) + 'd' + kernel_suffix, output.shape, parameters)

    # deal with 2D output images
    if copy_back_after_transforming:
        copy_slice(output, original_destination, 0)

    return original_destination