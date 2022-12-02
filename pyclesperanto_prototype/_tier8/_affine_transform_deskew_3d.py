from typing import Union

from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import push
from .._tier0 import create, create_like, create_none
from ._AffineTransform3D import AffineTransform3D
from skimage.transform import AffineTransform
from ._affine_transform import _determine_translation_and_bounding_box
import numpy as np
from enum import Enum


class DeskewDirection(Enum):
    X = 1
    Y = 2

@plugin_function(output_creator=create_none)
def affine_transform_deskew_3d(source: Image, destination: Image = None,
                               transform: Union[np.ndarray, AffineTransform3D, AffineTransform] = None,
                               deskewing_angle_in_degrees: float = 30,
                               voxel_size_x: float = 0.1449922,
                               voxel_size_y: float = 0.1449922,
                               voxel_size_z: float = 0.3,
                               deskew_direction: DeskewDirection = DeskewDirection.Y) -> Image:
    """
    Applies an affine transform to deskew an image. 
    Uses orthogonal interpolation (Sapoznik et al. (2020)  https://doi.org/10.7554/eLife.57681)

    Parameters
    ----------
    source : Image
        image to be transformed
    destination : Image, optional
        image where the transformed image should be written to
    transform : AffineTransform3D object, optional
        transform matrix or object or string describing the transformation
    deskewing_angle_in_degrees: float, optional
        Oblique plane or deskewing acquisition angle
    voxel_size_x: float, optional
        Pixel size in X axis in microns
    voxel_size_y: float, optional
        Pixel size in Y axis in microns
    voxel_size_z: float, optional
        Step size between image planes along coverslip in microns; Voxel size in Z in microns
    deskew_direction: str, optional
        Direction of skew, dependent on microscope configuration
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
    from .._tier0 import execute
    from .._tier0 import create

    assert len(source.shape) == 3, f"Image needs to be 3D, got shape of {len(source.shape)}"

    # handle output creation
    new_size, transform, _ = _determine_translation_and_bounding_box(source, transform)
    if destination is None:
        destination = create(new_size)
    
    # we invert the transform because we go from the target image to the source image to read pixels
    transform_matrix = np.asarray(transform.copy().inverse())

    # precalculate these functions that are dependent on deskewing angle
    tantheta = np.float32(np.tan(deskewing_angle_in_degrees * np.pi/180))
    sintheta = np.float32(np.sin(deskewing_angle_in_degrees * np.pi/180))
    costheta = np.float32(np.cos(deskewing_angle_in_degrees * np.pi/180))

    gpu_transform_matrix = push(transform_matrix)

    if deskew_direction == DeskewDirection.Y:
        kernel_suffix = 'deskew_y_'
        # change step size from physical space (nm) to camera space (pixels)
        pixel_step = np.float32(voxel_size_z/voxel_size_y)
    else:
        kernel_suffix = 'deskew_x_'
        # change step size from physical space (nm) to camera space (pixels)
        pixel_step = np.float32(voxel_size_z/voxel_size_x)

    # pass the shape of the final image, pixel step and precalculated trig

    parameters = {
        "input": source,
        "output": destination,
        "mat": gpu_transform_matrix,
        "pixel_step": pixel_step,
        "tantheta": tantheta,
        "costheta": costheta,
        "sintheta": sintheta
    }

    execute(__file__, './affine_transform_' + kernel_suffix + str(len(destination.shape)) + 'd' + '_x.cl',
            'affine_transform_'  + kernel_suffix + str(len(destination.shape)) + 'd', destination.shape, parameters)

    return destination
