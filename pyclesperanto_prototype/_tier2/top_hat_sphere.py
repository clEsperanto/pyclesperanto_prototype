from .._tier0 import create
from .._tier1 import minimum_sphere
from .._tier1 import maximum_sphere
from .._tier1 import add_images_weighted


def top_hat_sphere(input, output, radius_x, radius_y, radius_z=0):
    """Applies a top-hat filter for background subtraction to the input image.

    Available for: 2D, 3D

    Parameters
    ----------
    (Image input, ByRef Image destination, Number radiusX, Number radiusY, Number radiusZ)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_topHatSphere


    Returns
    -------

    """


    temp1 = create(input.shape);
    temp2 = create(input.shape);

    minimum_sphere(input, temp1, radius_x, radius_y, radius_z);
    maximum_sphere(temp1, temp2, radius_x, radius_y, radius_z);
    add_images_weighted(input, temp2, output, 1, -1);