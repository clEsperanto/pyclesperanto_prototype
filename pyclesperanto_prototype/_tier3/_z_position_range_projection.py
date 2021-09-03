from pyclesperanto_prototype._tier0 import plugin_function, Image, create_none, execute, create


@plugin_function(output_creator=create_none, categories=['projection'])
def z_position_range_projection(source_stack: Image, z_position: Image, destination: Image = None, start_z : int = -5, end_z : int = 5):
    """Project multiple Z-slices of a 3D stack into a new 3D stack.
    Which Z-slice is defined as the z_position image, which represents an altitude map.
    The two additional numbers define the range relative to the given z-position.

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
    ..[1] https://clij.github.io/clij2-docs/reference_zPositionRangeProjection
    """

    if destination is None:
        z_range = end_z - start_z + 1
        destination = create([z_range, source_stack.shape[-2], source_stack.shape[-1]])

    temp_position = create([source_stack.shape[-2], source_stack.shape[-1]])
    temp_slice = create([source_stack.shape[-2], source_stack.shape[-1]])

    from .._tier1 import add_image_and_scalar, copy_slice
    from .._tier2 import z_position_projection

    for i, z in enumerate(range(start_z, end_z + 1)):
        add_image_and_scalar(z_position, temp_position, z)
        z_position_projection(source_stack, temp_position, temp_slice)
        copy_slice(temp_slice, destination, i)

    return destination
