from ..core import execute


def crop(input, output, startx, starty, startz=0):
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
