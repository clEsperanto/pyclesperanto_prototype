from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(categories=['transform', 'in assistant'])
def scale(source : Image, destination : Image = None, factor_x : float = 1, factor_y : float = 1, factor_z : float = 1, centered : bool = True, linear_interpolation : bool = False):
    """Scale the image by given factors.

    Parameters
    ----------
    source : Image
        image to be translated
    destination : Image, optional
        target image
    factor_x : float
        scaling along x
    factor_y : float
        scaling along y
    factor_z : float
        scaling along z
    centered : bool
        If true, the image will be scaled to the center of the image.
        If false, the image will be scaled to the origin of the coordinate system.
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
    if centered:
        transform.center(source.shape)

    transform.scale(factor_x, factor_y, factor_z)

    if centered:
        transform.center(destination.shape, undo=True)

    return affine_transform(source, destination, transform, linear_interpolation)
