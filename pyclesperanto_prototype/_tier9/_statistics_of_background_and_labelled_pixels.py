from skimage.measure import regionprops

from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function
from .._tier0 import pull_zyx

@plugin_function(output_creator=create_none)
def statistics_of_background_and_labelled_pixels(input_image : Image, input_label_map : Image):
    from .._tier1 import add_image_and_scalar
    from .._tier9 import statistics_of_labelled_pixels

    temp = add_image_and_scalar(input_label_map, scalar=1)
    return statistics_of_labelled_pixels(input_image, temp)

