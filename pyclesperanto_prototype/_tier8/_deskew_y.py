from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_none


@plugin_function(output_creator=create_none)
def deskew_y(input_image: Image, output_image: Image = None, angle_in_degrees: float = 30) -> Image:
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

    Returns
    -------
    output_image
    """

    from ._AffineTransform3D import AffineTransform3D
    from ._affine_transform import affine_transform

    # shear in the X plane towards Y
    transform = AffineTransform3D()
    transform.shear_in_x_plane(angle_y_in_degrees=angle_in_degrees)

    # rotate the stack to get proper Z-planes
    transform.rotate(angle_in_degrees=angle_in_degrees, axis=0)

    # correct orientation so that the new Z-plane goes proximal-distal from the objective.
    transform.rotate(angle_in_degrees=90, axis=0)

    # apply transform
    return affine_transform(input_image, output_image, transform=transform, auto_size=True)