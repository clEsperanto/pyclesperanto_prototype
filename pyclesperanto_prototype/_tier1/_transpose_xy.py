from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import create_none
from .._tier0 import create
from .._tier0 import Image

@plugin_function(output_creator=create_none, categories=['transform'])
def transpose_xy(input : Image, destination : Image = None):
    """Transpose X and Y axes of an image.
    
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
    >>> cle.transpose_xy(input, destination)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_transposeXY
    """

    if destination is None:
        dimensions = input.shape
        if len(dimensions) == 3:
            destination = create([dimensions[0], dimensions[2], dimensions[1]])
        elif len(dimensions) == 2:
            destination = create([dimensions[1], dimensions[0]])
        elif len(dimensions) == 1:
            destination = create([dimensions[0], 1])

    parameters = {
        "src":input,
        "dst":destination
    }

    execute(__file__, '../clij-opencl-kernels/kernels/transpose_xy_3d_x.cl', 'transpose_xy_3d', destination.shape, parameters)

    return destination
