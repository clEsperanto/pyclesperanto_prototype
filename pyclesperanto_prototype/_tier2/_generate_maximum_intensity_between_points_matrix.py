from .._tier0 import execute, plugin_function, Image, create_none, create_matrix_from_pointlists, create_like


@plugin_function(output_creator=create_none)
def generate_maximum_intensity_between_points_matrix(intensity_image: Image, pointlist: Image, touch_matrix: Image = None,
                                                     maximum_intensity_matrix_destination: Image = None,
                                                     num_samples: int = 10):
    """Determine the maximum intensity between pairs of point coordinates and
    write them in a matrix.

    Parameters
    ----------
    intensity_image: Image
        image where the intensity will be measured
    pointlist: Image
        list of coordinates
    touch_matrix: Image, optional
        if only selected pairs should be measured, use this binary matrix to confige which
    maximum_intensity_matrix_destination: Image, optional
        matrix where the results are written ito
    num_samples: int, optional
        Number of samples to take along the line for averaging, default = 10

    Returns
    -------
    average_intensity_matrix_destination
    """
    from .._tier1 import set

    if maximum_intensity_matrix_destination is None:
        maximum_intensity_matrix_destination = create_matrix_from_pointlists(pointlist, pointlist)

    if touch_matrix is None:
        touch_matrix = create_like(maximum_intensity_matrix_destination)
        set(touch_matrix, 1)

    parameters = {
        "src_touch_matrix": touch_matrix,
        "src_pointlist": pointlist,
        "src_intensity": intensity_image,
        "dst_maximum_intensity_matrix": maximum_intensity_matrix_destination,
        "num_samples": int(num_samples)
    }

    execute(__file__, 'maximum_intensity_between_points_matrix_x.cl', 'maximum_intensity_between_points_matrix', touch_matrix.shape, parameters)

    return maximum_intensity_matrix_destination
