from .._tier0 import create_labels_like
from .._tier0 import plugin_function
from .._tier0 import Image


@plugin_function(categories=['label', 'in assistant'], output_creator=create_labels_like)
def gauss_otsu_labeling(source : Image, label_image_destination : Image = None, outline_sigma : float = 2) -> Image:
    """Labels objects directly from grey-value images.

    The outline_sigma parameter allows tuning the segmentation result. Under the hood,
    this filter applies a Gaussian blur, Otsu-thresholding [1] and connected component labeling [2]. The
    thresholded binary image is flooded using the Voronoi tesselation approach starting from the found local maxima.
    
    Parameters
    ----------
    source : Image
        Input grey-value image
    label_image_destination : Image, optional
        Output image
    outline_sigma : float, optional
        controls how precise segmented objects are outlined.
    
    Returns
    -------
    label_image_destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.gauss_otsu_labeling(source, label_image_destination, 2)
    
    References
    ----------
    .. [1] https://ieeexplore.ieee.org/document/4310076
    .. [2] https://en.wikipedia.org/wiki/Voronoi_diagram
    """
    from .._tier0 import create
    from .._tier1 import gaussian_blur
    from .._tier9 import threshold_otsu
    from .._tier4 import connected_components_labeling_box

    temp = create(source)
    gaussian_blur(source, temp, outline_sigma, outline_sigma, outline_sigma)

    segmentation = threshold_otsu(temp)

    label_image_destination = connected_components_labeling_box(segmentation)

    return label_image_destination
