from ..core import execute

def set_image_borders(output, scalar):
    """Sets all pixel values at the image border to a given value.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image destination, Number value)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_setImageBorders


    Returns
    -------

    """


    parameters = {
        "dst":output,
        "value":float(scalar)
    }

    execute(__file__, 'set_image_borders_' + str(len(output.shape)) + 'd_x.cl', 'set_image_borders_' + str(len(output.shape)) + 'd', output.shape, parameters);
