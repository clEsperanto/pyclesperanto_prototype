from pyclesperanto_prototype._tier0 import plugin_function, Image, create_2d_yx, execute

@plugin_function(output_creator = create_2d_yx, categories=['projection'])
def z_position_projection(source_stack : Image, z_position : Image, destination : Image = None):
    """Project a defined Z-slice of a 3D stack into a 2D image.

    Which Z-slice is defined as the z_position image, which represents an altitude map.

    Parameters
    ----------
    source_stack : Image
        Input image stack
    z_position : Image
        altitude map
    destination : Image, optional
        Projected image

    Returns
    -------
    destination

    See Also
    --------
    ..[1] https://clij.github.io/clij2-docs/reference_zPositionProjection
    """
    parameters = {
        "dst":destination,
        "position":z_position,
        "src":source_stack,
    }

    execute(__file__, 'z_position_projection_x.cl', 'z_position_projection', destination.shape, parameters)

    return destination

