from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['transform', 'in assistant'])
def shear(source : Image, destination : Image = None,
          angle_xy_in_degrees: float = 0,
          angle_xz_in_degrees: float = 0,
          angle_yx_in_degrees: float = 0,
          angle_yz_in_degrees: float = 0,
          angle_zx_in_degrees: float = 0,
          angle_zy_in_degrees: float = 0,
          linear_interpolation : bool = False):
    """Shear the image by given angles.

    Angles are given in degrees. To convert radians to degrees, use this formula:

    angle_in_degrees = angle_in_radians / numpy.pi * 180.0

    Parameters
    ----------
    source : Image
        image to be translated
    destination : Image, optional
        target image
    angle_xy_in_degrees : float, optional
        shearing along X-axis in XY plane according to given factor
    angle_xz_in_degrees : float, optional
        shearing along X-axis in XZ plane according to given factor
    angle_yx_in_degrees : float, optional
        shearing along Y-axis in XY plane according to given factor
    angle_yz_in_degrees : float, optional
        shearing along Y-axis in YZ plane according to given factor
    angle_zx_in_degrees : float, optional
        shearing along Z-axis in XZ plane according to given factor
    angle_zy_in_degrees : float, optional
        shearing along Z-axis in YZ plane according to given factor
    linear_interpolation: bool
        If true, bi-/tri-linear interpolation will be applied.
        If false, nearest-neighbor interpolation wille be applied.

    Returns
    -------
    destination

    """
    from ._AffineTransform3D import AffineTransform3D
    from ._affine_transform import affine_transform

    transform = AffineTransform3D()

    if angle_xy_in_degrees != 0 or angle_yx_in_degrees != 0:
        transform.shear_z(angle_xy_in_degrees, angle_yx_in_degrees)
    if angle_yz_in_degrees != 0 or angle_zy_in_degrees != 0:
        transform.shear_x(angle_yz_in_degrees, angle_zy_in_degrees)
    if angle_xz_in_degrees != 0 or angle_zx_in_degrees != 0:
        transform.shear_y(angle_xz_in_degrees, angle_zx_in_degrees)

    return affine_transform(source, destination, transform, linear_interpolation)
