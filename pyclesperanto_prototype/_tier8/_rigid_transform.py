from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def rigid_transform(source : Image, destination : Image = None, translate_x : float = 0, translate_y : float = 0, translate_z : float = 0, angle_around_x_in_degrees : float = 0, angle_around_y_in_degrees : float = 0, angle_around_z_in_degrees : float = 0, rotate_around_center : bool = True, linear_interpolation : bool = False):
    """Translate the image by a given vector and rotate it by given angles.

    Angles are given in degrees. To convert radians to degrees, use this formula:

    angle_in_degrees = angle_in_radians / numpy.pi * 180.0

    Parameters
    ----------
    source : Image
        image to be transformed
    destination : Image, optional
        target image
    translate_x : float
        translation along x axis in pixels
    translate_y : float
        translation along y axis in pixels
    translate_z : float
        translation along z axis in pixels
    angle_around_x_in_degrees : float
        rotation around x axis in radians
    angle_around_y_in_degrees : float
        rotation around y axis in radians
    angle_around_z_in_degrees : float
        rotation around z axis in radians
    rotate_around_center : boolean
        if True: rotate image around center (default)
        if False: rotate image around origin
    linear_interpolation: bool
        If true, bi-/tri-linear interplation will be applied.
        If false, nearest-neighbor interpolation wille be applied.

    Returns
    -------
    destination

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

    transform.translate(translate_x, translate_y, translate_z)

    return affine_transform(source, destination, transform, linear_interpolation)
