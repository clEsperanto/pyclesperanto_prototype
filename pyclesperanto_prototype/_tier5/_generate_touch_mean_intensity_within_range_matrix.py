from .._tier0 import plugin_function, Image, create_none
import numpy as np

@plugin_function(output_creator=create_none)
def generate_touch_mean_intensity_within_range_matrix(image: Image,
                                                      labels: Image,
                                                      touch_matrix_destination: Image = None,
                                                      minimum_intensity: float = 0,
                                                      maximum_intensity: float = np.finfo(np.float32).max):
    """Takes an image and a label image and determines whose label touch-borders lie within a given range.
    This results in a touch matrix.

    Notes
    -----
    * For technical reasons, only images of integer type are supported. In case images of type float are passed,
      the results may not be 100% repeatable.
    * The specified range includes minimum and maximum

    Parameters
    ----------
    image:Image
    labels:Image
    touch_matrix_destination:Image, optional
    minimum_intensity: float, optional
    maximum_intensity: float, optional

    Returns
    -------
    touch_matrix_destination
    """
    from .._tier1 import set_row, set_column, nan_to_num, replace_intensity, binary_and
    from .._tier3 import generate_touch_mean_intensity_matrix
    from .._tier2 import maximum_of_all_pixels

    # measure intensity along borders
    tmi_matrix = generate_touch_mean_intensity_matrix(image, labels)
    #print("tmi2225", tmi_matrix[22,25])

    # do not merge anything with background
    set_column(tmi_matrix, 0, minimum_intensity - 1)
    set_row(tmi_matrix, 0, minimum_intensity - 1)

    # do not merge anything that doesn't touch
    temp = nan_to_num(tmi_matrix)
    temp = replace_intensity(temp, value_to_replace=0, value_replacement=minimum_intensity - 1)

    # determine which should be merged

    #print("maximum_intensity_", maximum_intensity)
    touch_matrix_destination = binary_and(temp >= minimum_intensity, temp <= maximum_intensity, touch_matrix_destination)

    #print("bm2225", touch_matrix_destination[22,25])

    return touch_matrix_destination
