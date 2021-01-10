from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
from pyclesperanto_prototype._tier0 import create_none
from .._tier0 import plugin_function
from .._tier0 import create_vector_from_labelmap

@plugin_function(output_creator=create_vector_from_labelmap)
def read_intensities_from_map(labels : Image, map_image : Image, values_destination : Image = None):
    """Takes a label image and an parametric image and reads parametric values from the labels positions.
    The read intensity valus are stored in a new vector.

    Note: This will only work if all labels have number of voxels == 1 or if all pixels in each label have the same value.

    Parameters
    ----------
    labels
    map_image
    values_destination

    Returns
    -------

    """
    from .._tier0 import execute
    from .._tier1 import set

    set(values_destination, 0)

    parameters = {
        "labels": labels,
        "map_image":map_image,
        "intensities":values_destination
    }

    execute(__file__, 'read_intensities_from_map_x.cl', 'read_intensities_from_map', labels.shape, parameters)
    return values_destination