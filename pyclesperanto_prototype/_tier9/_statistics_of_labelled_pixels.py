from skimage.measure import regionprops

from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function

@plugin_function(output_creator=create_none)
def statistics_of_labelled_pixels(input : Image = None, labelmap : Image = None, extra_properties = []):
    """Determines bounding box, area (in pixels/voxels), min, max, mean and standard deviation
    intensity of labelled objects in a label map and corresponding pixels in the
    original image. 
    
    Instead of a label map, you can also use a binary image as a binary image is a 
    label map with just one label.
    
    This method is executed on the CPU and not on the GPU/OpenCL device. Under the hood, it uses
    skimage.measure.regionprops [2] and thus, offers the same output. Additionally, `standard_deviation_intensity` and
    is stored in the `regionprops` object.
    
    Parameters
    ----------
    input : Image
    labelmap : Image
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_statisticsOfLabelledPixels
    .. [2] https://scikit-image.org/docs/stable/api/skimage.measure.html#skimage.measure.regionprops
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

    # Inspired by: https://forum.image.sc/t/how-to-measure-standard-deviation-of-intensities-with-scikit-image-regionprops/46948/2
    import numpy as np

    # arguments must be in the specified order, matching regionprops
    def standard_deviation_intensity(region, intensities):
        return np.std(intensities[region])

    extra_properties.append(standard_deviation_intensity)

    props = regionprops(label_image, intensity_image=intensity_image, cache=True, extra_properties=extra_properties)

    return props

