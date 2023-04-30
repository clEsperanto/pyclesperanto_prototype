from pyclesperanto_prototype._tier0 import plugin_function, Image, create_2d_zx, execute

@plugin_function(output_creator = create_2d_zx, categories=['projection', 'in assistant'])
def y_position_of_maximum_y_projection(source : Image, destination : Image = None) -> Image:
    """Determines an Y-position of the maximum intensity along Y and writes it into the resulting image.

    If there are multiple y-slices with the same value, the smallest Y will be chosen.

    Parameters
    ----------
    source : Image
        Input image stack
    destination : Image, optional
        altitude map

    Returns
    -------
    destination

    See Also
    --------
    ..[1] https://clij.github.io/clij2-docs/reference_zPositionOfMaximumZProjection
    """
    parameters = {
        "dst_arg":destination,
        "src":source,
    }

    execute(__file__, 'y_position_of_maximum_y_projection_x.cl', 'y_position_of_maximum_y_projection', destination.shape, parameters)

    return destination
