from .._tier2 import maximum_of_all_pixels
from .._tier0 import create_pointlist_from_labelmap
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_pointlist_from_labelmap)
def labelled_spots_to_pointlist(input_labelled_spots:Image, destination_pointlist :Image = None):
    """Generates a coordinate list of points in a labelled spot image. 
    
    Transforms a labelmap of spots (single pixels with values 1, 2, ..., n for n 
    spots) as resulting 
    from connected components analysis in an image where every column contains d 
    pixels (with d = dimensionality of the original image) with the coordinates of 
    the maxima/minima. 
    
    Parameters
    ----------
    input_labelled_spots : Image
    destination_pointlist : Image
    
    Returns
    -------
    destination_pointlist
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_labelledSpotsToPointList
    """

    parameters = {
        "src":input_labelled_spots,
        "dst_point_list":destination_pointlist
    }

    # todo: make naming conventions fit
    execute(__file__, '../clij-opencl-kernels/kernels/labelled_spots_to_point_list_x.cl', 'labelled_spots_to_point_list', input_labelled_spots.shape, parameters)

    return destination_pointlist
