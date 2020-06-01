from ..core import execute

def set_ramp_x(output):
    """Sets all pixel values to their X coordinate

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_setRampX


    Returns
    -------

    """


    parameters = {
        "dst":output
    }

    execute(__file__, 'set_ramp_x_' + str(len(output.shape)) + 'd_x.cl', 'set_ramp_x_' + str(len(output.shape)) + 'd', output.shape, parameters);
