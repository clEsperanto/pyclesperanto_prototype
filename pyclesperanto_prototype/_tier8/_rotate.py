from .._tier0 import plugin_function
from .._tier0 import Image, create_none

@plugin_function(categories=['transform', 'in assistant'], output_creator=create_none)
def rotate(
        source: Image,
        destination: Image = None,
        angle_around_x_in_degrees: float = 0,
        angle_around_y_in_degrees: float = 0,
        angle_around_z_in_degrees: float = 0,
        rotate_around_center: bool = True,
        linear_interpolation: bool = False,
        auto_size: bool = False):
    """Rotate the image by given angles.

    Angles are given in degrees. To convert radians to degrees, use this formula:

    angle_in_degrees = angle_in_radians / numpy.pi * 180.0

    Parameters
    ----------
    source : Image
        image to be translated
    destination : Image, optional
        target image
    angle_around_x_in_degrees : float, optional
        rotation around x axis in degrees
    angle_around_y_in_degrees : float, optional
        rotation around y axis in degrees
    angle_around_z_in_degrees : float, optional
        rotation around z axis in degrees
    rotate_around_center : bool, optional
        if True: rotate image around center
        if False: rotate image around origin
    linear_interpolation: bool, optional
        If true, bi-/tri-linear interpolation will be applied, if hardware supports it.
        If false, nearest-neighbor interpolation wille be applied.
    auto_size: bool, optional
        Automatically determines the size of the output image depending on the rotation angles.
        If set to True, the rotate_around_center setting is not relevant.
        Note: auto_size will be ignored if destination is not None. For more details see [1].

    Returns
    -------
    destination

    See Also
    --------
    ..[1] affine_transform
    """
    from ._AffineTransform3D import AffineTransform3D
    from ._affine_transform import affine_transform

    transform = AffineTransform3D()
    if rotate_around_center:
        transform.center(source.shape)

    if angle_around_x_in_degrees != 0:
        transform.rotate(0, angle_around_x_in_degrees)
    if angle_around_y_in_degrees != 0:
        transform.rotate(1, angle_around_y_in_degrees)
    if angle_around_z_in_degrees != 0:
        transform.rotate(2, angle_around_z_in_degrees)

    if rotate_around_center:
        transform.center(source.shape, undo=True)

    return affine_transform(source, destination, transform, linear_interpolation, auto_size)
