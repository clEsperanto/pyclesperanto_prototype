from .._tier0 import Image
from .._tier0 import plugin_function

@plugin_function
def statistics_of_image(image : Image):
    """Determines image size (bounding box), area (in pixels/voxels), min, max, mean and standard deviation of the
    intensity of all pixels in the original image.

    This method is executed on the CPU and not on the GPU/OpenCL device. Under the hood, it uses
    skimage.measure.regionprops [2] and thus, offers the same output. Additionally, `standard_deviation_intensity` is
    stored in the `regionprops` object.

    Parameters
    ----------
    image

    Returns
    -------
    regionprops of the whole image

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_statisticsOfImage
    .. [2] https://scikit-image.org/docs/stable/api/skimage.measure.html#skimage.measure.regionprops

    """
    from .._tier0 import create_like
    from .._tier1 import set
    from .._tier9 import statistics_of_labelled_pixels

    binary_image = create_like(image)
    set(binary_image, 1)

    return statistics_of_labelled_pixels(image, binary_image)