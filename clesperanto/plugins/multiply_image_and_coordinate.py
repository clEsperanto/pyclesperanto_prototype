from ..core import radius_to_kernel_size
from ..core import execute

def multiply_image_and_coordinate(input, output, dimension):
    """Multiplies all pixel intensities with the x, y or z coordinate, depending on specified dimension.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number dimension)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_multiplyImageAndCoordinate


    Returns
    -------

    """


    parameters = {
        "src":input,
        "dst":output,
        "dimension":int(dimension)
    };

    execute(__file__, 'multiply_image_and_coordinate_' + str(len(output.shape)) + 'd_x.cl', 'multiply_image_and_coordinate_' + str(len(output.shape)) + 'd', output.shape, parameters);

