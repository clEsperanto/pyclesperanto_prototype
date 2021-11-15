from .._tier1 import set
from .._tier0 import plugin_function
from .._tier0 import create
from .._tier0 import Image
from .._tier0 import execute, create_labels_like
from .._tier1 import sum_x_projection
from .._tier1 import sum_y_projection

@plugin_function(categories=['label', 'in assistant'], output_creator=create_labels_like)
def label_spots(input_spots : Image, labelled_spots_destination : Image = None):
    """Transforms a binary image with single pixles set to 1 to a labelled 
    spots image. 
    
    Transforms a spots image as resulting from maximum/minimum detection in an image 
    of the same size where every spot has a number 1, 2, ... n. 
    
    Parameters
    ----------
    input_spots : Image
    labelled_spots_destination : Image
    
    Returns
    -------
    labelled_spots_destination
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_labelSpots
    """

    set(labelled_spots_destination, 0)

    dimensionality = input_spots.shape
    if (len(dimensionality) == 2):  # 2D image
        dimensionality = [1, dimensionality[0], dimensionality[1]]

    spot_count_per_x = create([dimensionality[1], dimensionality[2]])

    sum_x_projection(input_spots, spot_count_per_x)

    spot_count_per_xy = create([dimensionality[1], dimensionality[2]])

    sum_y_projection(spot_count_per_x, spot_count_per_xy)

    dims = [dimensionality[0], dimensionality[1], 1]

    parameters = {
        "dst": labelled_spots_destination,
        "src": input_spots,
        "spotCountPerX": spot_count_per_x,
        "spotCountPerXY": spot_count_per_xy
    }

    execute(__file__, 'label_spots_in_x.cl', 'label_spots_in_x', dims, parameters)

    return labelled_spots_destination