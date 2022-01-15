from typing import Union

from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push
from .._tier0 import create, create_like, create_none
from ._AffineTransform3D import AffineTransform3D
from skimage.transform import AffineTransform
import numpy as np

@plugin_function(output_creator=create_none)
def affine_transform(source : Image, destination : Image = None, transform : Union[np.ndarray, AffineTransform3D, AffineTransform] = None, linear_interpolation : bool = False, auto_size:bool = False):
    """
    Applies an affine transform to an image.

    Parameters
    ----------
    source : Image
        image to be transformed
    destination : Image, optional
        image where the transformed image should be written to
    transform : 4x4 numpy array or AffineTransform3D object or skimage.transform.AffineTransform object, optional
        transform matrix or object describing the transformation
    linear_interpolation: bool, optional
        If true, bi-/tri-linear interplation will be applied; if hardware supports it.
        If false, nearest-neighbor interpolation wille be applied.
    auto_size:bool, optional
        If true, the destination image size will be determined automatically, depending on the provided transform.
        the transform might be modified so that all voxels of the result image have positions x>=0, y>=0, z>=0 and sit
        tight to the coordinate origin. No voxels will cropped, the result image will fit in the returned destination.
        Hence, the applied transform may have an additional translation vector that was not explicitly provided. This
        also means that any given translation vector will be neglected.
        If false, the destination image will have the same size as the input image.
        Note: The value of auto-size is ignored if: destination is not None or transform is not an instance of
        AffineTransform3D.

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

    # handle output creation
    if destination is None:
        if auto_size and isinstance(transform, AffineTransform3D):
            # This modifies the given transform
            new_size, transform, _ = _determine_translation_and_bounding_box(source, transform)
            print("determined translation", _)
            print("determined new_size", new_size)
            destination = create(new_size)
        else:
            destination = create_like(source)

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
        # Question: Don't we have to invert this one as well? haesleinhuepf
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


def _determine_translation_and_bounding_box(source: Image, affine_transformation: AffineTransform3D):
    """Starting from a given input image and an affine transform, we compute the output size of the new image
    and a translation vector that it necessary to keep all pixels in positive coordinates.

    Parameters
    ----------
    source: Image
        The image to be transformed
    affine_transformation: AffineTransform3D
        The transform to be applied

    Returns
    -------
    new_shape: tuple(int)
        Size of output image
    new_affine_transform: AffineTransform3D
        Modified transform so that all pixels remain in positive coordinates
    translation: tuple(int)
        Translation vector that is necessary to keep all pixels in positive coordinates
    """

    # define coordinates of all corners of the current stack
    from itertools import product
    nx, ny, nz = source.shape
    original_bounding_box = [list(x) + [1] for x in product((0, nz), (0, ny), (0, nx))]
    # transform the corners using the given affine transform
    transformed_bounding_box = np.asarray(list(map(lambda x: affine_transformation._matrix @ x, original_bounding_box)))

    # the min and max coordinates tell us from where to where the image ranges (bounding box)
    min_coordinate = transformed_bounding_box.min(axis=0)
    max_coordinate = transformed_bounding_box.max(axis=0)
    # determine the size of the transformed bounding box
    new_shape = (max_coordinate - min_coordinate)[0:3].astype(int).tolist()[::-1]

    # we make a copy to not modify the original transform
    new_affine_transform = AffineTransform3D()
    new_affine_transform.concatenate(affine_transformation)

    # if the new minimum-coordinate is `-x`, we need to
    # translate the stack by `x` so that the new origin is (0,0,0)
    translation = -min_coordinate
    new_affine_transform.translate(
        translate_x=translation[0],
        translate_y=translation[1],
        translate_z=translation[2]
    )

    return new_shape, new_affine_transform, translation[0:3]
