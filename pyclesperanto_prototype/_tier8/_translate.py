from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def translate(source : Image, destination : Image = None, translate_x : float = 0, translate_y : float = 0, translate_z : float = 0):
    from ._AffineTransform3D import AffineTransform3D
    from ._affine_transform import affine_transform

    transform = AffineTransform3D()
    transform.translate(translate_x, translate_y, translate_z)

    return affine_transform(source, destination, transform)
