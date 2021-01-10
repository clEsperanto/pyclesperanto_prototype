from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def scale(source : Image, destination : Image = None, factor_x : float = 1, factor_y : float = 1, factor_z : float = 1, centered=True):
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
    centered

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
        transform.center(source.shape, undo=True)

    return affine_transform(source, destination, transform)
