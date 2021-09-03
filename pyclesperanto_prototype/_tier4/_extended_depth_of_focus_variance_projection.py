from .._tier0 import plugin_function, Image, create_2d_xy

@plugin_function(output_creator = create_2d_xy, categories=['projection'])
def extended_depth_of_focus_variance_projection(source : Image, destination : Image = None, radius_x : int = 10, radius_y : int = 10, sigma : float = 5):
    """Extended depth of focus projection maximizing local pixel intensity variance.

    Parameters
    ----------
    source : Image
    destination : Image, optional
    radius_x : int
        radius of a sphere where the variance should be determined
    radius_y : int
        radius of a sphere where the variance should be determined
    sigma : float
        The sigma parameter allows controlling a Gaussian blur which smoothes the altitude map.

    Returns
    -------
    destination
    """
    from .._tier1 import variance_sphere, gaussian_blur
    from .._tier2 import z_position_of_maximum_z_projection, z_position_projection
    variance = variance_sphere(source, radius_x=radius_x, radius_y=radius_y, radius_z=0)

    temp = gaussian_blur(variance, sigma_x=sigma, sigma_y=sigma, sigma_z=0)
    del variance

    altitude = z_position_of_maximum_z_projection(temp)
    del temp

    destination = z_position_projection(source, altitude, destination)

    return destination