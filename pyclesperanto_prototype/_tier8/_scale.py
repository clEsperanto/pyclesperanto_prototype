from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_none

@plugin_function(output_creator=create_none)
def scale(source : Image, output : Image = None, factor_x : float = 1, factor_y : float = 1, factor_z : float = 1, centered=True, zoom = None):
    """Scale the image by given factors.

    Parameters
    ----------
    source : Image
        image to be translated
    output : Image, optional
        target image
    factor_x : float
        scaling along x
    factor_y : float
        scaling along y
    factor_z : float
        scaling along z
    centered : bool
        if True the image is scaled towards its center (default)
        if False it will be scaled towards the origin
    zoom : float or sequence
        The zoom factor along the axes (ignoring centering). If a float, zoom is the
        same for each axis. If a sequence, zoom should contain
        one value for each axis.

    Returns
    -------
    destination

    """
    from ._AffineTransform3D import AffineTransform3D
    from ._affine_transform import affine_transform
    from .._tier0 import create

    if output is None:
        import numpy as np
        dimensions = np.asarray(source.shape)

        # Todo: I'm sure the following block could be shorter.
        if len(dimensions) == 3:
            dimensions[0] = dimensions[0] * factor_z
            dimensions[1] = dimensions[1] * factor_y
            dimensions[2] = dimensions[2] * factor_x
            if zoom is not None:
                if isinstance(zoom, float) or isinstance(zoom, int):
                    dimensions[0] = dimensions[0] * zoom
                    dimensions[1] = dimensions[1] * zoom
                    dimensions[2] = dimensions[2] * zoom
                else:
                    dimensions[0] = dimensions[0] * zoom[0]
                    dimensions[1] = dimensions[1] * zoom[1]
                    dimensions[2] = dimensions[2] * zoom[2]
        else: # 2D image
            dimensions[0] = dimensions[0] * factor_y
            dimensions[1] = dimensions[1] * factor_x
            if zoom is not None:
                if isinstance(zoom, float) or isinstance(zoom, int):
                    dimensions[0] = dimensions[0] * zoom
                    dimensions[1] = dimensions[1] * zoom
                else:
                    dimensions[0] = dimensions[0] * zoom[0]
                    dimensions[1] = dimensions[1] * zoom[1]
        output = create(dimensions)

    transform = AffineTransform3D()
    if centered:
        transform.center(source.shape)

    transform.scale(factor_x, factor_y, factor_z)

    if centered:
        transform.center(source.shape, undo=True)

    if zoom is not None:
        import numpy as np
        #zoom = np.asarray(zoom, dtype=np.float32)
        #zoom = 1 / zoom
        if isinstance(zoom, float) or isinstance(zoom, int):
            if len(source.shape) == 3:
                transform.scale(zoom, zoom, zoom)
            else: # 2D image
                transform.scale(zoom, zoom)
        else:
            zoom.reverse()
            transform.scale(*zoom)

    return affine_transform(source, output, transform)
