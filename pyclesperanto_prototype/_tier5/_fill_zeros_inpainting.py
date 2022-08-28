from .._tier0 import Image
from .._tier0 import plugin_function

@plugin_function(categories=['filter', 'in assistant'])
def fill_zeros_inpainting(source : Image, destination : Image = None) -> Image:
    """Replaces 0 pixels in an image with neighboring intensities (if not 0) iteratively until no 0-value pixels are
    left. This operation can also be called nearest-neighbor inpainting.

    Parameters
    ----------
    source: Image
    destination: Image, optional

    Returns
    -------
    destination

    See Also
    --------
    * extend_labeling_via_voronoi
    """
    from .._tier4 import extend_labeling_via_voronoi
    return extend_labeling_via_voronoi(source, destination)
