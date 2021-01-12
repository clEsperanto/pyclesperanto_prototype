from skimage.measure import regionprops

from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function
from .._tier0 import pull

@plugin_function(output_creator=create_none)
def statistics_of_background_and_labelled_pixels(input : Image = None, labelmap : Image = None):
    """Determines bounding box, area (in pixels/voxels), min, max and mean 
    intensity of background and labelled objects in a label map and corresponding
    pixels in the original image.
    
    Instead of a label map, you can also use a binary image as a binary image is a 
    label map with just one label.
    
    This method is executed on the CPU and not on the GPU/OpenCL device. 
    
    Parameters
    ----------
    input : Image
    labelmap : Image

    Returns
    -------
    Dictionary of measurements
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_statisticsOfBackgroundAndLabelledPixels
    """
    from .._tier1 import add_image_and_scalar
    from .._tier9 import statistics_of_labelled_pixels

    temp = add_image_and_scalar(labelmap, scalar=1)
    regionprops = statistics_of_labelled_pixels(input, temp)

    if isinstance(regionprops, dict):
        # correct regionprops label
        regionprops['original_label'] = regionprops['label'] - 1

    else:
        # correct regionprops label
        for r in regionprops:
            r.original_label = r.label - 1

    return regionprops



