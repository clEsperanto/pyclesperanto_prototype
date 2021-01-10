from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def rotate(source : Image, destination : Image = None, angle_around_x_in_rad : float = 0, angle_around_y_in_rad : float = 0, angle_around_z_in_rad : float = 0, rotate_around_center=True):
    """Rotate the image by given angles.

    Angles are given in radians. To convert degrees in radians, use this formula:

    angle_in_rad = angle_in_deg * numpy.pi / 180.0

    Parameters
    ----------
    source : Image
        image to be translated
    destination : Image, optional
        target image
    angle_around_x_in_rad : float
        rotation around x axis in radians
    angle_around_y_in_rad : float
        rotation around y axis in radians
    angle_around_z_in_rad : float
        rotation around z axis in radians

    Returns
    -------
    destination

    """
    from ._AffineTransform3D import AffineTransform3D
    from ._affine_transform import affine_transform

    transform = AffineTransform3D()
    if rotate_around_center:
        transform.center(source.shape)

    if angle_around_x_in_rad != 0:
        transform.rotate(0, angle_around_x_in_rad)
    if angle_around_y_in_rad != 0:
        transform.rotate(1, angle_around_y_in_rad)
    if angle_around_z_in_rad != 0:
        transform.rotate(2, angle_around_z_in_rad)

    if rotate_around_center:
        transform.center(source.shape, undo=True)


    return affine_transform(source, destination, transform)
