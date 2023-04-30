import warnings
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_none


@plugin_function(output_creator=create_none, categories=['transform', 'in assistant'])
def deskew_x(input_image: Image,
             output_image: Image = None,
             angle_in_degrees: float = 31.8,
             voxel_size_x: float = 1,
             voxel_size_y: float = 1,
             voxel_size_z: float = 1,
             scale_factor: float = 1,
             linear_interpolation: bool = True
             ) -> Image:
    """
    Deskew an image stack as acquired with oblique plane light-sheet microscopy, with skew in the X direction.

    Parameters
    ----------
    input_image: Image
        raw image data with Z-planes representing the tilted / swept acquisition plane
    output_image: Image, optional
        reconstructed image data with Z-planes in proximal-distal oriental from the objective
    angle_in_degrees: float, optional
        default: 31.8 degrees
    voxel_size_x: float, optional
    voxel_size_y: float, optional
    voxel_size_z: float, optional
        default: 1 micron
        Voxel size, typically provided in microns
    scale_factor: float, optional
        default: 1
        If the resulting image becomes too huge, it is possible to reduce output image size by this factor.
        The isotropic voxel size of the output image will then be voxel_size_x / scaling_factor.
    linear_interpolation: bool, optional
        If True (default), uses orthogonal interpolation (Sapoznik et al. (2020)  https://doi.org/10.7554/eLife.57681)
        If False, nearest-neighbor interpolation wille be applied.

    Returns
    -------
    output_image
    """
    if not linear_interpolation:
        warnings.warn("linear_interpolation = False is deprecated due to deskewing artifacts. The linear_interpolation parameter will be removed in a future version.")

    from ._AffineTransform3D import AffineTransform3D
    from ._affine_transform import affine_transform
    from ._affine_transform_deskew_3d import affine_transform_deskew_3d, DeskewDirection

    # define affine transformation
    transform = AffineTransform3D()
    transform._deskew_x(angle_in_degrees=angle_in_degrees, voxel_size_x=voxel_size_x, voxel_size_y=voxel_size_y,
                        voxel_size_z=voxel_size_z, scale_factor=scale_factor)

    # apply transform
    if linear_interpolation:
        return affine_transform_deskew_3d(source=input_image, destination=output_image,
                                          transform=transform,
                                          deskewing_angle_in_degrees=angle_in_degrees,
                                          voxel_size_x=voxel_size_x,
                                          voxel_size_y=voxel_size_y,
                                          voxel_size_z=voxel_size_z,
                                          deskew_direction=DeskewDirection.X)
    else:
        return affine_transform(input_image, output_image, transform=transform, auto_size=True,
                                linear_interpolation=False)
