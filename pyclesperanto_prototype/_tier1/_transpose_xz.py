from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import create_none
from .._tier0 import create
from .._tier0 import Image

@plugin_function(output_creator=create_none)
def transpose_xz(src : Image , dst : Image = None):
    """Transpose X and Z axes of an image.
    
    Parameters
    ----------
    input : Image
        The input image.
    destination : Image
        The output image where results are written into.
         
    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.transpose_xz(input, destination)
    >>>     
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_transposeXZ    

    """

    if dst is None:
        dimensions = src.shape
        if len(dimensions) == 3:
            dst = create(dimensions[::-1])
        elif len(dimensions) == 2:
            dst = create([dimensions[1], dimensions[0], 1])
        elif len(dimensions) == 1:
            dst = create([dimensions[0], 1, 1])

    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'transpose_xz_3d_x.cl', 'transpose_xz_3d', dst.shape, parameters)

    return dst
