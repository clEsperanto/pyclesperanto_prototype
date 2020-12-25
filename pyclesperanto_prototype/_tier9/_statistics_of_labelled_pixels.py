from skimage.measure import regionprops

from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function

@plugin_function(output_creator=create_none)
def statistics_of_labelled_pixels(input : Image = None, labelmap : Image = None):
    """Determines bounding box, area (in pixels/voxels), min, max and mean 
    intensity 
     of labelled objects in a label map and corresponding pixels in the 
    original image. 
    
    Instead of a label map, you can also use a binary image as a binary image is a 
    label map with just one label.
    
    This method is executed on the CPU and not on the GPU/OpenCL device. 
    
    Parameters
    ----------
    input : Image
    labelmap : Image
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_statisticsOfLabelledPixels
    """
    from .._tier0 import create_like
    from .._tier0 import pull_zyx
    from .._tier0 import push_zyx
    from .._tier1 import replace_intensities
    from .._tier3 import squared_difference

    if labelmap is None:
        raise Exception("A label image must be provided")

    label_image = pull_zyx(labelmap).astype(int)
    if input is None:
        intensity_image = label_image
    else:
        intensity_image = pull_zyx(input)

    props = regionprops(label_image, intensity_image=intensity_image, cache=True)

    import numpy as np

    means = [element.mean_intensity for element in props]
    mean_vector = push_zyx(np.asarray(means))

    temp1 = create_like(input)
    temp2 = create_like(input)
    replace_intensities(labelmap, mean_vector, temp1)
    squared_difference(input, temp1, temp2)
    var_intensity_image = pull_zyx(temp2)
    var_props = regionprops(label_image, intensity_image=var_intensity_image, cache=True)

    for element, var_element in zip(props, var_props):
        element.variance_intensity = var_element.mean_intensity
        element.standard_deviation_intensity = np.sqrt(var_element.mean_intensity)

    return props

