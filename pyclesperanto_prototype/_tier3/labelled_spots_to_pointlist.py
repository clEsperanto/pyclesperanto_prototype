from .._tier2 import maximum_of_all_pixels
from .._tier0 import create_pointlist_from_labelmap
from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_pointlist_from_labelmap)
def labelled_spots_to_pointlist(label_map:Image, pointlist:Image = None):

    """
    documentation placeholder
    """

    parameters = {
        "src":label_map,
        "dst_point_list":pointlist
    }

    # todo: make naming conventions fit
    execute(__file__, 'labelled_spots_to_point_list_x.cl', 'labelled_spots_to_point_list', label_map.shape, parameters)

    return pointlist
