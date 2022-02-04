from numpy import angle
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_none


@plugin_function(output_creator=create_none)
def deskew_y(input_image: Image,
             output_image: Image = None,
             angle_in_degrees: float = 30,
             voxel_size_x: float = 1,
             voxel_size_y: float = 1,
             voxel_size_z: float = 1,
             scaling_factor: float = 1
             ) -> Image:
    """
    Deskew an image stack as aquired with single-objective light-sheet microscopy.

    Parameters
    ----------
    input_image: Image
        raw image data with Z-planes representing the swept acquisition plane
    output_image: Image, optional
        reconstructed image data with Z-planes in proximal-distal oriental from the objective
    angle_in_degrees: float, optional
        default: 30 degrees
    voxel_size_x: float, optional
    voxel_size_y: float, optional
    voxel_size_z: float, optional
         default: 1 micron
         Voxel size, typically provided in microns
    scaling_factor: float, optional
        default: 1
        If the resulting image becomes too huge, it is possible to reduce output image size by this factor.
        The voxel size of the output image will then be voxel_size_x / scaling_factor.

    Returns
    -------
    output_image
    """

    from ._AffineTransform3D import AffineTransform3D
    from ._affine_transform import affine_transform
    import math
    
    # shear in the X plane towards Y
    transform = AffineTransform3D()
    transform._deskew_y(angle_in_degrees=angle_in_degrees, voxel_size_x=voxel_size_x, voxel_size_y=voxel_size_y,
                       voxel_size_z=voxel_size_z, scaling_factor=scaling_factor)

    # apply transform
    return affine_transform(input_image, output_image, transform=transform, auto_size=True)
