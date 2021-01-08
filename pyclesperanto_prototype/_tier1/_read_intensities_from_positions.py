from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import create_none
from .._tier0 import plugin_function

@plugin_function(output_creator=create_none)
def read_intensities_from_positions(pointlist : Image, intensity_image : Image, values_destination : Image = None):
    """Go to positions in a given image specified by a pointlist and read intensities of those pixels. The intensities
    are stored in a new vector.

    Parameters
    ----------
    pointlist
    intensity_image
    values_destination

    Returns
    -------

    """
    from .._tier0 import execute
    from .._tier0 import create

    if values_destination is None:
        values_destination = create([1, pointlist.shape[1]])

    parameters = {
        "pointlist": pointlist,
        "input":intensity_image,
        "intensities":values_destination
    }

    execute(__file__, 'read_intensities_from_positions_x.cl', 'read_intensities_from_positions', values_destination.shape, parameters)
    return values_destination