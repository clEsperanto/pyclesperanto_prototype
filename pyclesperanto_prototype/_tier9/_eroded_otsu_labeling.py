from .._tier0 import plugin_function, Image, create_labels_like

@plugin_function(categories=['label', 'in assistant'], output_creator=create_labels_like)
def eroded_otsu_labeling(image: Image, labels_destination: Image = None, number_of_erosions: int = 5, outline_sigma: float = 2) -> Image:
    """Segments and labels an image using blurring, Otsu-thresholding, binary erosion and
    masked Voronoi-labeling.

    After bluring and Otsu-thresholding the image, iterative binary erosion is applied.
    Objects in the eroded image are labeled and the labels are extended to fit again into
    the initial binary image using masked-Voronoi labeling.

    This function is similar to voronoi_otsu_labeling. It is intended to deal better in
    case labels of objects swapping into each other if objects are dense. Like when using
    Voronoi-Otsu-labeling, small objects may disappear when applying this operation.

    This function is inspired by a similar implementation in Java by Jan Brocher (Biovoxxel) [0] [1]

    Parameters
    ----------
    image: Image
        intensity image
    labels_destination: Image,optional
        output label image
    number_of_erosions: int, optional
        Number of iterations for an erosion. This number must be smaller than the smallest radius
        of the objects to segment. If the radius is too high, objects may disappear.
    outline_sigma: float, optional
        Before thresholding, a Gaussian blur is applied using this sigma for smoothing the outline.

    Returns
    -------
    label_image: Image
    """

    """
    See also
    --------
    ..[0] https://github.com/biovoxxel/bv3dbox/blob/9e38ed02cff606e7e8fbe57db0f6af810bf1a83a/BioVoxxel_3D_Box/src/main/java/de/biovoxxel/bv3dbox/plugins/BV_LabelSplitter.java#L83
    ..[1] https://zenodo.org/badge/latestdoi/434949702
    """
    from .._tier0 import create_like
    from .._tier1 import gaussian_blur, copy, erode_box
    from .._tier9 import threshold_otsu
    from .._tier5 import masked_voronoi_labeling

    # initial thresholding
    blurred = gaussian_blur(image, sigma_x=outline_sigma, sigma_y=outline_sigma, sigma_z=outline_sigma)
    binary = threshold_otsu(blurred)

    # iterative erosion
    eroded = copy(binary)
    eroded1 = create_like(binary)
    for i in range(int(number_of_erosions)):
        eroded1 = erode_box(eroded, eroded1)
        eroded, eroded1 = eroded1, eroded

    # labeling, label extension
    return masked_voronoi_labeling(eroded, binary, labels_destination)
