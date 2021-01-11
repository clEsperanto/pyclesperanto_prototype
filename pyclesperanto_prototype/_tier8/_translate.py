from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def translate(source : Image, destination : Image = None, translate_x : float = 0, translate_y : float = 0, translate_z : float = 0, shift = None):
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
    shift : float or sequence
        The shift along the axes. If a float, `shift` is the same for each
        axis. If a sequence, `shift` should contain one value for each axis.

    Returns
    -------
    destination

    """
    from ._AffineTransform3D import AffineTransform3D
    from ._affine_transform import affine_transform

    transform = AffineTransform3D()
    transform.translate(translate_x, translate_y, translate_z)

    if shift is not None:
        if isinstance(shift, float) or isinstance(shift, int):
            if len(source.shape) == 3:
                transform.translate(shift, shift, shift)
            else: #  2D image
                transform.translate(shift, shift)
        else:
            shift.reverse()
            transform.translate(*shift)

    return affine_transform(source, destination, transform)
