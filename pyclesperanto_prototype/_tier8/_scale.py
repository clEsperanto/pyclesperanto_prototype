from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_none, create_like

@plugin_function(categories=['transform', 'in assistant'], output_creator=create_none)
def scale(source: Image,
          destination: Image = None,
          factor_x: float = 1,
          factor_y: float = 1,
          factor_z: float = 1,
          centered: bool = True,
          linear_interpolation: bool = False,
          auto_size: bool = False) -> Image:
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
    auto_size: bool, optional
        Automatically determines the size of the output image depending on the rotation angles.
        If set to True, the centered setting is not relevant.
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
    if centered and not auto_size:
        transform.center(source.shape)

    transform.scale(factor_x, factor_y, factor_z)

    if centered and not auto_size:
        transform.center(destination.shape, undo=True)

    return affine_transform(source, destination, transform, linear_interpolation, auto_size)
