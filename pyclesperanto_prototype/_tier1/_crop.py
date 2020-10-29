from .._tier0 import execute
from .._tier0 import create
from .._tier0 import create_none
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_none)
def crop(input : Image, output : Image = None, startx : int = 0, starty : int = 0, startz : int = 0, width : int = 1, height : int = 1, depth : int = 1):
    """Crops a given rectangle out of a given image

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number scalar)
    todo: Better documentation will follow
          In the meantime, read more: 2D: https://clij.github.io/clij2-docs/reference_crop2D
                                      3D: https://clij.github.io/clij2-docs/reference_crop3D


    Returns
    -------

    """

    if output is None:
        output = create([depth, height, width])

    parameters = {
            "dst": output,
            "src": input,
            "start_x": int(startx),
            "start_y": int(starty),
        }
    if len(input.shape) == 3:
        # 3D image
        parameters.update({"start_z": int(startz)})

    execute(__file__, 'crop_' + str(len(output.shape)) + 'd_x.cl', 'crop_' + str(len(output.shape)) + 'd', output.shape, parameters)
    return output
