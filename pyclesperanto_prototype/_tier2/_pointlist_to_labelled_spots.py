from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import add_images_weighted
from .._tier1 import write_values_to_positions
from .._tier0 import create
from .._tier0 import create_from_pointlist
from .._tier1 import paste
from .._tier1 import set_ramp_x
from .._tier1 import add_image_and_scalar

@plugin_function(output_creator=create_from_pointlist)
def pointlist_to_labelled_spots(pointlist : Image, labelled_spots_destination : Image = None):
    """

    Parameters
    ----------
    pointlist
    labelled_spots_destination

    Returns
    -------

    """

    temp1 = create([pointlist.shape[0] + 1, pointlist.shape[1]])
    temp2 = create([pointlist.shape[0] + 1, pointlist.shape[1]])

    set_ramp_x(temp1)
    add_image_and_scalar(temp1, temp2, 1)
    paste(pointlist, temp2)
    from .._tier1 import set
    set(labelled_spots_destination, 0)
    labelled_spots_destination = write_values_to_positions(temp2, labelled_spots_destination)

    return labelled_spots_destination