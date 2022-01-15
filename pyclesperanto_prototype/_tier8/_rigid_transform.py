from .._tier0 import plugin_function
from .._tier0 import Image, create_none, create_like

@plugin_function(categories=['transform', 'in assistant'], output_creator=create_none)
def rigid_transform(
        source: Image,
        destination: Image = None,
        translate_x: float = 0,
        translate_y: float = 0,
        translate_z: float = 0,
        angle_around_x_in_degrees: float = 0,
        angle_around_y_in_degrees: float = 0,
        angle_around_z_in_degrees: float = 0,
        rotate_around_center: bool = True,
        linear_interpolation: bool = False,
        auto_size: bool = False):
    """Translate the image by a given vector and rotate it by given angles.

    Angles are given in degrees. To convert radians to degrees, use this formula:

    angle_in_degrees = angle_in_radians / numpy.pi * 180.0

    Parameters
    ----------
    source : Image
        image to be transformed
    destination : Image, optional
        target image
    translate_x : float, optional
        translation along x axis in pixels
    translate_y : float, optional
        translation along y axis in pixels
    translate_z : float, optional
        translation along z axis in pixels
    angle_around_x_in_degrees : float, optional
        rotation around x axis in radians
    angle_around_y_in_degrees : float, optional
        rotation around y axis in radians
    angle_around_z_in_degrees : float, optional
        rotation around z axis in radians
    rotate_around_center : bool, optional
        if True: rotate image around center (default)
        if False: rotate image around origin
    linear_interpolation: bool, optional
        If true, bi-/tri-linear interpolation will be applied, if hardware allows.
        If false, nearest-neighbor interpolation wille be applied.
    auto_size: bool, optional
        Automatically determines the size of the output image depending on the rotation angles.
        If set to True, the rotate_around_center setting is not relevant. The applied transform may have an additional
        translation vector that was not explicitly provided. This also means that any given translation vector will be
        neglected.
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

    if destination is None and not auto_size:
        destination = create_like(source)

    transform = AffineTransform3D()
    if rotate_around_center:
        transform.center(source.shape)

    if angle_around_x_in_degrees != 0:
        transform.rotate(0, angle_around_x_in_degrees)
    if angle_around_y_in_degrees != 0:
        transform.rotate(1, angle_around_y_in_degrees)
    if angle_around_z_in_degrees != 0:
        transform.rotate(2, angle_around_z_in_degrees)

    if rotate_around_center and not auto_size:
        transform.center(destination.shape, undo=True)

    transform.translate(translate_x, translate_y, translate_z)

    return affine_transform(source, destination, transform, linear_interpolation, auto_size)
