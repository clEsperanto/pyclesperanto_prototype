from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def rotate(source : Image, destination : Image = None, angle_around_x_in_degrees : float = 0, angle_around_y_in_degrees : float = 0, angle_around_z_in_degrees : float = 0, rotate_around_center=True, angle : float = None, axes = None):
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
        rotation around x axis in radians
    angle_around_y_in_degrees : float, optional
        rotation around y axis in radians
    angle_around_z_in_degrees : float, optional
        rotation around z axis in radians
    rotate_around_center : boolean, optional
        if True: rotate image around center (default)
        if False: rotate image around origin
    angle : float, optional
        The rotation angle in degrees.
    axes : tuple of 2 ints, optional
        The two axes that define the plane of rotation. Default is the first two axes.

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


    if angle is not None and axes is not None:
        # adapted from https://github.com/scipy/scipy/blob/v1.6.0/scipy/ndimage/interpolation.py#L886
        ndim = source.ndim

        if ndim < 2:
            raise ValueError('input array should be at least 2D')

        axes = list(axes)

        if len(axes) != 2:
            raise ValueError('axes should contain exactly two values')

        if not all([float(ax).is_integer() for ax in axes]):
            raise ValueError('axes should contain only integer values')

        if axes[0] < 0:
            axes[0] += ndim
        if axes[1] < 0:
            axes[1] += ndim
        if axes[0] < 0 or axes[1] < 0 or axes[0] >= ndim or axes[1] >= ndim:
            raise ValueError('invalid rotation plane specified')

        axes.sort()

        if axes == [0, 1]:
            transform.rotate(0, -angle)
        if axes == [0, 2]:
            transform.rotate(1, angle)
        if axes == [1, 2]:
            transform.rotate(2, -angle)

    if rotate_around_center:
        transform.center(source.shape, undo=True)

    return affine_transform(source, destination, transform)
