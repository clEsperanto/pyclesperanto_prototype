from .._tier0 import plugin_function, Image, create_2d_xy

@plugin_function(output_creator = create_2d_xy, categories=['projection', 'in assistant'])
def extended_depth_of_focus_sobel_projection(source : Image, destination : Image = None, sigma : float = 5):
    """Extended depth of focus projection maximizing intensity int the local sobel image.

    Parameters
    ----------
    source : Image
    destination : Image, optional
    sigma : float
        The sigma parameter allows controlling a Gaussian blur which smoothes the altitude map.

    Returns
    -------
    destination
    """
    from .._tier1 import sobel, gaussian_blur
    from .._tier2 import z_position_of_maximum_z_projection, z_position_projection
    variance = sobel(source)

    temp = gaussian_blur(variance, sigma_x=sigma, sigma_y=sigma, sigma_z=0)
    del variance

    altitude = z_position_of_maximum_z_projection(temp)
    del temp

    destination = z_position_projection(source, altitude, destination)

    return destination