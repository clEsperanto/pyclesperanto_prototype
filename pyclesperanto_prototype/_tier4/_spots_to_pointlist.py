from .._tier2 import maximum_of_all_pixels
from .._tier0 import create_none
from .._tier0 import create
from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier2 import label_spots
from .._tier3 import labelled_spots_to_pointlist

@plugin_function(output_creator=create_none)
def spots_to_pointlist(input_spots:Image, destination_pointlist :Image = None):
    """

    Parameters
    ----------
    input_spots
    destination_pointlist

    Returns
    -------

    """
    labelled_spots = label_spots(input_spots)

    destination_pointlist = labelled_spots_to_pointlist(labelled_spots, destination_pointlist)

    return destination_pointlist
