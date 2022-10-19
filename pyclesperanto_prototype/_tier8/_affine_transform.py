from itertools import combinations_with_replacement
from typing import Union

from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push
from .._tier0 import create, create_like, create_none
from ._AffineTransform3D import AffineTransform3D
from skimage.transform import AffineTransform
import numpy as np

@plugin_function(output_creator=create_none)
def affine_transform(source : Image, destination : Image = None,
                     transform : Union[np.ndarray, AffineTransform3D, AffineTransform] = None,
                     linear_interpolation : bool = False, auto_size:bool = False) -> Image:
    """
    Applies an affine transform to an image.

    Parameters
    ----------
    source : Image
        image to be transformed
    destination : Image, optional
        image where the transformed image should be written to
    transform : 4x4 numpy array or AffineTransform3D object or skimage.transform.AffineTransform object or str, optional
        transform matrix or object or string describing the transformation
    linear_interpolation: bool, optional
        If true, bi-/tri-linear interplation will be applied; if hardware supports it.
        If false, nearest-neighbor interpolation wille be applied.
    auto_size:bool, optional
        If true, modifies the transform and the destination image size will be determined automatically, depending on the provided transform.
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

    # handle output creation
    if auto_size and isinstance(transform, AffineTransform3D):
        new_size, transform, _ = _determine_translation_and_bounding_box(source, transform)
    if destination is None:
        if auto_size and isinstance(transform, AffineTransform3D):
            # This modifies the given transform
            destination = create(new_size)
        else:
            destination = create_like(source)

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

    if isinstance(transform, str):
        transform = AffineTransform3D(transform, source)

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
        else:
            from .._tier0 import _warn_of_interpolation_not_available
            _warn_of_interpolation_not_available()
        source = image

    parameters = {
        "input": source,
        "output": destination,
        "mat": gpu_transform_matrix,
    }
    #print("parameters", parameters)
    #adding line for testing kernel
    kernel_suffix = ''
    execute(__file__, './affine_transform_' + str(len(destination.shape)) + 'd' + kernel_suffix + '_x.cl',
            'affine_transform_' + str(len(destination.shape)) + 'd' + kernel_suffix, destination.shape, parameters)

    # deal with 2D output images
    if copy_back_after_transforming:
        copy_slice(destination, original_destination, 0)

    return original_destination

@plugin_function(output_creator=create_none)
def affine_transform_opm(source : Image, destination : Image = None,
                     transform : Union[np.ndarray, AffineTransform3D, AffineTransform] = None,
                     deskewing_angle_in_degrees: float = 30,
                     linear_interpolation : bool = False, auto_size:bool = False) -> Image:
    """
    Applies an affine transform to an image.

    Parameters
    ----------
    source : Image
        image to be transformed
    destination : Image, optional
        image where the transformed image should be written to
    transform : 4x4 numpy array or AffineTransform3D object or skimage.transform.AffineTransform object or str, optional
        transform matrix or object or string describing the transformation
    linear_interpolation: bool, optional
        If true, bi-/tri-linear interplation will be applied; if hardware supports it.
        If false, nearest-neighbor interpolation wille be applied.
    auto_size:bool, optional
        If true, modifies the transform and the destination image size will be determined automatically, depending on the provided transform.
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

    # handle output creation
    if auto_size and isinstance(transform, AffineTransform3D):
        new_size, transform, _ = _determine_translation_and_bounding_box(source, transform)
    if destination is None:
        if auto_size and isinstance(transform, AffineTransform3D):
            # This modifies the given transform
            destination = create(new_size)
        else:
            destination = create_like(source)

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

    if isinstance(transform, str):
        transform = AffineTransform3D(transform, source)

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

    # precalculate trig functions for scan angle
    tantheta = np.float32(np.tan(deskewing_angle_in_degrees * np.pi/180)) # (float32)
    sintheta = np.float32(np.sin(deskewing_angle_in_degrees * np.pi/180)) # (float32)
    costheta = np.float32(np.cos(deskewing_angle_in_degrees * np.pi/180)) # (float32)
    
    gpu_transform_matrix = push(transform_matrix)

    kernel_suffix = ''
    if linear_interpolation:
        image = empty_image_like(source)
        copy(source, image)
        if type(source) != type(image):
            kernel_suffix = '_interpolate'
        else:
            from .._tier0 import _warn_of_interpolation_not_available
            _warn_of_interpolation_not_available()
        source = image

    parameters = {
        "input": source,
        "output": destination,
        "mat": gpu_transform_matrix,
        "tantheta": float(tantheta),
        "costheta": float(costheta),
        "sintheta": float(sintheta)
    }
    #print("parameters", parameters)
    #adding line for testing kernel
    kernel_suffix = ''
    execute(__file__, './affine_transform_' + 'opm' + kernel_suffix + '.cl',
            'affine_transform_' + 'opm'+ kernel_suffix, destination.shape, parameters)

    # deal with 2D output images
    if copy_back_after_transforming:
        copy_slice(destination, original_destination, 0)

    return original_destination



@plugin_function(output_creator=create_none)
def affine_transform_deskew(source : Image,
                            destination : Image = None,
                            transform : Union[np.ndarray, AffineTransform3D, AffineTransform] = None,
                            shear_transform : Union[np.ndarray, AffineTransform3D, AffineTransform] = None,
                            translate_mat_1 : Union[np.ndarray, AffineTransform3D, AffineTransform] = None,
                            translate_mat_2 : Union[np.ndarray, AffineTransform3D, AffineTransform] = None,
                            translate_mat_3 : Union[np.ndarray, AffineTransform3D, AffineTransform] = None,
                            translate_mat_4 : Union[np.ndarray, AffineTransform3D, AffineTransform] = None,
                            linear_interpolation : bool = False,
                            auto_size:bool = False) -> Image:
    """
    Applies an affine transform to an image.

    Parameters
    ----------
    source : Image
        image to be transformed
    destination : Image, optional
        image where the transformed image should be written to
    transform : 4x4 numpy array or AffineTransform3D object or skimage.transform.AffineTransform object or str, optional
        transform matrix or object or string describing the transformation
    linear_interpolation: bool, optional
        If true, bi-/tri-linear interplation will be applied; if hardware supports it.
        If false, nearest-neighbor interpolation wille be applied.
    auto_size:bool, optional
        If true, modifies the transform and the destination image size will be determined automatically, depending on the provided transform.
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

    # handle output creation
    if auto_size and isinstance(transform, AffineTransform3D):
        new_size, transform, _ = _determine_translation_and_bounding_box(source, transform)
    if destination is None:
        if auto_size and isinstance(transform, AffineTransform3D):
            # This modifies the given transform
            destination = create(new_size)
        else:
            destination = create_like(source)

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

    if isinstance(transform, str):
        transform = AffineTransform3D(transform, source)

    # we invert the transform because we go from the target image to the source image to read pixels
    if isinstance(transform, AffineTransform3D):
        transform_matrix = np.asarray(transform.copy().inverse())
        shear_mat_inv = np.asarray(shear_transform.copy().inverse())
        shear_mat = np.asarray(shear_transform.copy())
        translate_mat_yz1 = np.asarray(translate_mat_1.copy())
        translate_mat_yz2 = np.asarray(translate_mat_2.copy())
        translate_mat_yz3 = np.asarray(translate_mat_3.copy())
        translate_mat_yz4 = np.asarray(translate_mat_4.copy())
        
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
    shear_mat = push(shear_mat)
    translate_mat_yz1 = push(translate_mat_yz1)
    translate_mat_yz2= push(translate_mat_yz2)
    translate_mat_yz3 = push(translate_mat_yz3)
    translate_mat_yz4 = push(translate_mat_yz4)
    shear_mat_inv = push(shear_mat_inv)
    
    kernel_suffix = ''
    if linear_interpolation:
        image = empty_image_like(source)
        copy(source, image)
        if type(source) != type(image):
            kernel_suffix = '_interpolate_test'
        else:
            from .._tier0 import _warn_of_interpolation_not_available
            _warn_of_interpolation_not_available()
        source = image

    parameters = {
        "input": source,
        "output": destination,
        "mat": gpu_transform_matrix,
        "shear_mat": shear_mat,
        "shear_mat_inv": shear_mat_inv,
        "translate_mat_yz1": translate_mat_yz1,
        "translate_mat_yz2": translate_mat_yz2,
        "translate_mat_yz3": translate_mat_yz3,
        "translate_mat_yz4": translate_mat_yz4
    }
    #print("parameters", parameters)
    #adding line for testing kernel
    #kernel_suffix = ''
    execute(__file__, './affine_transform_' + str(len(destination.shape)) + 'd' + kernel_suffix + '_x.cl',
            'affine_transform_' + str(len(destination.shape)) + 'd' + kernel_suffix, destination.shape, parameters)
    
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
    if len(source.shape) == 2:
        ny, nz = source.shape
        nx = 1
    else:
        nx, ny, nz = source.shape

    original_bounding_box = [list(x) + [1] for x in product((0, nz), (0, ny), (0, nx))]
    # transform the corners using the given affine transform
    transformed_bounding_box = np.asarray(list(map(lambda x: affine_transformation._matrix @ x, original_bounding_box)))

    # the min and max coordinates tell us from where to where the image ranges (bounding box)
    min_coordinate = transformed_bounding_box.min(axis=0)
    max_coordinate = transformed_bounding_box.max(axis=0)
    # determine the size of the transformed bounding box
    new_shape = np.around((max_coordinate - min_coordinate)[0:3]).astype(int).tolist()[::-1]

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

    if len(source.shape) == 2:
        return new_shape[1:], new_affine_transform, translation[1:3]
    else:
        return new_shape, new_affine_transform, translation[0:3]
