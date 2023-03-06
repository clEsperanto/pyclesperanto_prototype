from pyclesperanto_prototype._tier0 import plugin_function, Image, create_2d_yz, execute

@plugin_function(output_creator = create_2d_yz, categories=['projection', 'in assistant'])
def x_position_of_minimum_x_projection(source : Image, destination : Image = None) -> Image:
    """Determines an X-position of the minimum intensity along X and writes it into the resulting image.

    If there are multiple x-slices with the same value, the smallest X will be chosen.

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
    ..[1] https://clij.github.io/clij2-docs/reference_zPositionOfMinimumZProjection
    """
    parameters = {
        "dst_arg":destination,
        "src":source,
    }

    execute(__file__, 'x_position_of_minimum_x_projection_x.cl', 'x_position_of_minimum_x_projection', destination.shape, parameters)

    return destination
