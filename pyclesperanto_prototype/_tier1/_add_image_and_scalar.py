from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def add_image_and_scalar(input : Image, output : Image = None, scalar : float = 1):
    """Adds a scalar value s to all pixels x of a given image X.
    
    <pre>f(x, s) = x + s</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number scalar)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_addImageAndScalar


    Returns
    -------

    """


    parameters = {
        "src":input,
        "dst":output,
        "scalar":float(scalar)
    }
    execute(__file__, 'add_image_and_scalar_' + str(len(output.shape)) + 'd_x.cl', 'add_image_and_scalar_' + str(len(output.shape)) + 'd', output.shape, parameters)

    return output
