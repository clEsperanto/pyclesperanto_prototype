from pyclesperanto_prototype._tier0 import plugin_function, Image, create_2d_yx, execute

@plugin_function(output_creator = create_2d_yx, categories=['projection', 'in assistant'])
def z_position_of_maximum_z_projection(source : Image, destination : Image = None):
    """Determines a Z-position of the maximum intensity along Z and writes it into the resulting image.

    If there are multiple z-slices with the same value, the smallest Z will be chosen.

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

    execute(__file__, 'z_position_of_maximum_z_projection_x.cl', 'z_position_of_maximum_z_projection', destination.shape, parameters)

    return destination
