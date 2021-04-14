from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['transform', 'in assistant'])
def translate(source : Image, destination : Image = None, translate_x : float = 0, translate_y : float = 0, translate_z : float = 0, linear_interpolation : bool = False):
    """Translate the image by a given vector.

    Parameters
    ----------
    source : Image
        image to be translated
    destination : Image, optional
        target image
    translate_x : float
        translation along x axis in pixels
    translate_y : float
        translation along y axis in pixels
    translate_z : float
        translation along z axis in pixels
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
    transform.translate(translate_x, translate_y, translate_z)

    return affine_transform(source, destination, transform, linear_interpolation)
