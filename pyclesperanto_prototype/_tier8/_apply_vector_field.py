from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier0 import create_none

@plugin_function(output_creator=create_none)
def apply_vector_field(source : Image, vector_x : Image, vector_y : Image, vector_z : Image = None, destination : Image = None, linear_interpolation : bool = False):
    """
    Deforms an image stack according to distances provided in the given vector image stacks.

    Parameters
    ----------
    source : Image
        The input image to be processed.
    vector_x : Image
        Pixels in this image describe the distance in X direction pixels should be shifted during warping.
    vector_y : Image
        Pixels in this image describe the distance in Y direction pixels should be shifted during warping.
    vector_z : Image
        Pixels in this image describe the distance in Z direction pixels should be shifted during warping.
    destination : Image
        The output image where results are written into.

    Returns
    -------
    destination

    """
    from .._tier0 import empty_image_like
    from .._tier0 import execute
    from .._tier1 import copy
    from .._tier0 import create_like

    if destination is None:
        destination = create_like(source)

    kernel_suffix = ''
    if linear_interpolation:
        image = empty_image_like(source)
        copy(source, image)
        if type(source) != type(image):
            kernel_suffix = '_interpolate'
        source = image

    if len(destination.shape) == 2:
        parameters = {
            "src": source,
            "vectorX": vector_x,
            "vectorY": vector_y,
            "dst": destination,
        }
    else:
        parameters = {
            "src": source,
            "vectorX": vector_x,
            "vectorY": vector_y,
            "vectorZ": vector_z,
            "dst": destination,
        }

    execute(__file__, '../clij-opencl-kernels/kernels/apply_vectorfield_' + str(len(destination.shape)) + 'd' + kernel_suffix + '_x.cl',
            'apply_vectorfield_' + str(len(destination.shape)) + 'd' + kernel_suffix, destination.shape, parameters)

    return destination