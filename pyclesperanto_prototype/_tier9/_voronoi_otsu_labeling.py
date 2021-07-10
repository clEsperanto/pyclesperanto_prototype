from .. import minimum_of_all_pixels, maximum_of_all_pixels
from .._tier0 import pull, create_labels_like
from .._tier1 import greater_constant

import numpy as np

from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier3 import histogram

@plugin_function(categories=['label', 'in assistant'], priority=1, output_creator=create_labels_like)
def voronoi_otsu_labeling(source : Image, label_image_destination : Image = None, spot_sigma : float = 2, outline_sigma : float = 2):
    """Labels objects directly from grey-value images.

    The two sigma parameters allow tuning the segmentation result. Under the hood,
    this filter applies two Gaussian blurs, spot detection, Otsu-thresholding [2] and Voronoi-labeling [3]. The
    thresholded binary image is flooded using the Voronoi tesselation approach starting from the found local maxima.
    
    Parameters
    ----------
    source : Image
        Input grey-value image
    label_image_destination : Image, optional
        Output image
    spot_sigma : float
        controls how close detected cells can be
    outline_sigma : float
        controls how precise segmented objects are outlined.
    
    Returns
    -------
    label_image_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.voronoi_otsu_labeling(source, label_image_destination, 10, 2)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_voronoiOtsuLabeling
    .. [2] https://ieeexplore.ieee.org/document/4310076
    .. [3] https://en.wikipedia.org/wiki/Voronoi_diagram
    """
    from .._tier0 import create
    from .._tier1 import detect_maxima_box
    from .._tier1 import gaussian_blur
    from .._tier9 import threshold_otsu
    from .._tier1 import mask
    from .._tier1 import binary_and
    from .._tier5 import masked_voronoi_labeling

    temp = create(source)
    gaussian_blur(source, temp, spot_sigma, spot_sigma, spot_sigma)

    spots = create(source)
    detect_maxima_box(temp, spots, 0, 0, 0)

    gaussian_blur(source, temp, outline_sigma, outline_sigma, outline_sigma)

    segmentation = create(source)
    threshold_otsu(temp, segmentation)

    binary = binary_and(spots, segmentation)

    masked_voronoi_labeling(binary, segmentation, temp)
    mask(temp, segmentation, label_image_destination)

    return label_image_destination
