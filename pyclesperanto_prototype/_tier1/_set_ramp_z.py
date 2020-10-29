from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def set_ramp_z(output : Image):
    """Sets all pixel values to their Z coordinate

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_setRampZ


    Returns
    -------

    """


    parameters = {
        "dst":output
    }

    execute(__file__, 'set_ramp_z_' + str(len(output.shape)) + 'd_x.cl', 'set_ramp_z_' + str(len(output.shape)) + 'd', output.shape, parameters);
    return output