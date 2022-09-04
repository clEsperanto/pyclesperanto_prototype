from numpy import angle
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_none


@plugin_function(output_creator=create_none, categories=['transform', 'in assistant'])
def deskew_y(input_image: Image,
             output_image: Image = None,
             angle_in_degrees: float = 30,
             voxel_size_x: float = 1,
             voxel_size_y: float = 1,
             voxel_size_z: float = 1,
             scale_factor: float = 1
             ) -> Image:
    """
    Deskew an image stack as acquired with oblique plane light-sheet microscopy.

    Parameters
    ----------
    input_image: Image
        raw image data with Z-planes representing the tilted / swept acquisition plane
    output_image: Image, optional
        reconstructed image data with Z-planes in proximal-distal oriental from the objective
    angle_in_degrees: float, optional
        default: 30 degrees
    voxel_size_x: float, optional
    voxel_size_y: float, optional
    voxel_size_z: float, optional
         default: 1 micron
         Voxel size, typically provided in microns
    scale_factor: float, optional
        default: 1
        If the resulting image becomes too huge, it is possible to reduce output image size by this factor.
        The isotropic voxel size of the output image will then be voxel_size_x / scaling_factor.

    Returns
    -------
    output_image
    """

    # this is a workaround step, see https://github.com/clEsperanto/pyclesperanto_prototype/issues/172
    # resolved by defining shear factor based on voxel in _deskew_y()
    #from ._scale import scale
    #scaled_image = scale(input_image, factor_z=voxel_size_z / 0.3, auto_size=True)
    #voxel_size_z = 0.3

    from ._AffineTransform3D import AffineTransform3D
    from ._affine_transform import affine_transform
    
    # shear in the X plane towards Y
    transform = AffineTransform3D()
    transform._deskew_y(angle_in_degrees=angle_in_degrees, voxel_size_x=voxel_size_x, voxel_size_y=voxel_size_y,
                        voxel_size_z=voxel_size_z, scale_factor=scale_factor)

    # apply transform
    return affine_transform(input_image, output_image, transform=transform, auto_size=True,linear_interpolation=True)

