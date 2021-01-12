from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function

@plugin_function(output_creator=create_none)
def regionprops(labelmap : Image, intensity_image : Image = None, cache : bool = True, extra_properties = []):
    """Convert the intensity image and the corresponding label image to numpy arrays (via pull) and calls scikit-image
    regionprops [1]. Hence, this operation runs on the CPU. A faster, GPU-accelerated function with limited measurements
    is available as statistics_of_labelled_pixels [2].

    Note: the parameter order is different compared to statistics_of_labeled_pixels

    Parameters
    ----------
    labelmap : Image
    intensity_image : Image
    extra_properties : list

    Returns
    -------
    scikit-image regionprops

    References
    ----------
    .. [1] https://scikit-image.org/docs/stable/api/skimage.measure.html#skimage.measure.regionprops
    .. [2] https://clij.github.io/clij2-docs/reference_statisticsOfLabelledPixels
    """

    from .._tier0 import pull

    if labelmap is None:
        raise Exception("A label image must be provided")

    label_image = pull(labelmap).astype(int)
    if intensity_image is not None:
        intensity_image = pull(intensity_image)

    # Inspired by: https://forum.image.sc/t/how-to-measure-standard-deviation-of-intensities-with-scikit-image-regionprops/46948/2
    import numpy as np

    # arguments must be in the specified order, matching regionprops
    def standard_deviation_intensity(region, intensities):
        return np.std(intensities[region])

    extra_properties.append(standard_deviation_intensity)

    from skimage import measure
    props = measure.regionprops(label_image, intensity_image=intensity_image, cache=cache, extra_properties=extra_properties)

    # save regionprops label
    for r in props:
        r.original_label = r.label

    return props
