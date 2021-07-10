from .. import minimum_of_all_pixels, maximum_of_all_pixels
from .._tier0 import pull, create_binary_like
from .._tier1 import greater_constant

import numpy as np

from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier3 import histogram

@plugin_function(categories=['binarize', 'in assistant'], priority=1, output_creator=create_binary_like)
def threshold_otsu(input : Image, destination : Image = None):
    """Binarizes an image using Otsu's threshold method [3] implemented in scikit-image[2]
    using a histogram determined on the GPU to create binary images.
    
    Parameters
    ----------
    input : Image
    destination : Image
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.threshold_otsu(input, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_thresholdOtsu
    .. [2] https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.threshold_otsu
    .. [3] https://ieeexplore.ieee.org/document/4310076
    """

    # build a bin-centers array for scikit-image
    minimum_intensity = minimum_of_all_pixels(input)
    maximum_intensity = maximum_of_all_pixels(input)

    range = maximum_intensity - minimum_intensity

    bin_centers = np.arange(256) * range / (255)

    # Determine histogram on GPU
    hist = pull(histogram(input, num_bins=256, minimum_intensity=minimum_intensity, maximum_intensity=maximum_intensity, determine_min_max=False))

    # determine threshold using scikit-image
    threshold = scikit_image_threshold_otsu(hist=(hist, bin_centers))

    # print(str(threshold))

    # apply the threshold on the GPU
    destination = greater_constant(input, destination, threshold)

    return destination






# This function lives here temporarily
def scikit_image_threshold_otsu(image=None, nbins=256, *, hist=None):

    if image is None and hist is None:
        raise Exception("Either name or hist must be provided.")

    if hist is not None:
        if isinstance(hist, (tuple, list)):
            counts, bin_centers = hist
        else:
            counts = hist
            bin_centers = np.arange(counts.size)
    else:
        if image.ndim > 2 and image.shape[-1] in (3, 4):
            msg = "threshold_otsu is expected to work correctly only for " \
                  "grayscale images; image shape {0} looks like an RGB image"
            print(msg.format(image.shape))

        # Check if the image is multi-colored or not
        first_pixel = image.ravel()[0]
        if np.all(image == first_pixel):
            return first_pixel

        counts, bin_centers = histogram(image.ravel(), nbins, source_range='image')

    counts = counts.astype(float)

    # class probabilities for all possible thresholds
    weight1 = np.cumsum(counts)
    weight2 = np.cumsum(counts[::-1])[::-1]
    # class means for all possible thresholds
    mean1 = np.cumsum(counts * bin_centers) / weight1
    mean2 = (np.cumsum((counts * bin_centers)[::-1]) / weight2[::-1])[::-1]

    # Clip ends to align class 1 and class 2 variables:
    # The last value of ``weight1``/``mean1`` should pair with zero values in
    # ``weight2``/``mean2``, which do not exist.
    variance12 = weight1[:-1] * weight2[1:] * (mean1[:-1] - mean2[1:]) ** 2

    idx = np.argmax(variance12)

    threshold = bin_centers[:-1][idx]

    return threshold