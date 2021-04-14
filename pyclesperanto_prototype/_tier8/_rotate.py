from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['transform', 'in assistant'])
def rotate(source : Image, destination : Image = None, angle_around_x_in_degrees : float = 0, angle_around_y_in_degrees : float = 0, angle_around_z_in_degrees : float = 0, rotate_around_center : bool = True, linear_interpolation : bool = False):
    """Rotate the image by given angles.

    Angles are given in degrees. To convert radians to degrees, use this formula:

    angle_in_degrees = angle_in_radians / numpy.pi * 180.0

    Parameters
    ----------
    source : Image
        image to be translated
    destination : Image, optional
        target image
    angle_around_x_in_degrees : float
        rotation around x axis in radians
    angle_around_y_in_degrees : float
        rotation around y axis in radians
    angle_around_z_in_degrees : float
        rotation around z axis in radians
    rotate_around_center : boolean
        if True: rotate image around center
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

    return affine_transform(source, destination, transform, linear_interpolation)
