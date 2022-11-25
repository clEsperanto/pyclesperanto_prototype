from skimage import morphology
import numpy as np
from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_like
from .._tier1 import absolute
from .._tier1 import binary_or
from .._tier1 import binary_not
from .._tier1 import gradient_x
from .._tier1 import gradient_y
from .._tier1 import gradient_z
from .._tier1 import greater_constant
from .._tier1 import mask
from .._tier2 import opening_sphere

@plugin_function
def morphological_snakes(input_image: Image, 
                        contour_image : Image = np.zeros((0, 0)), 
                        output_image : Image = None, 
                        n_iter : int = 100, 
                        smoothing : int = 1, 
                        lambda1 : float = 1, 
                        lambda2 : float = 1) -> Image:
    """
    Parameters
    ----------
    input_iamge: Image
    contour_image: Image, optional
    output_image: Image, optional
    n_iter: int, optional
    smoothing: int, optional
    lambda1: int, optional
    lambda2: int, optional

    Returns
    -------
    Final segmentation

    """

    if contour_image.size == 0:
        contour_image = checkerboard_level_set(input_image.shape)
    
    greater_constant(contour_image, destination=output_image, constant=0)

    for _ in range(n_iter):
        
        invert_curve = 1 - output_image
        outside_image = (input_image * invert_curve).sum()
        outside_curve_area = invert_curve.sum() + 1e-8
        c0 = outside_image / outside_curve_area

        inside_image = (input_image * output_image).sum()
        inside_curve_area = output_image.sum() + 1e-8
        c1 = inside_image / inside_curve_area

        absolute_gradient = create_like(output_image)
        for d in range(input_image.ndim):
            if d == 0:   
                absolute_gradient += absolute(gradient_x(output_image))
            if d == 1:
                absolute_gradient += absolute(gradient_y(output_image))
            if d == 2:
                absolute_gradient += absolute(gradient_z(output_image))

        current_curve = absolute_gradient * (lambda1 * (input_image - c1)**2 - lambda2 * (input_image - c0)**2)
        positive_curve = current_curve > 0
        negative_curve = current_curve < 0

        combined_mask = binary_or(positive_curve, negative_curve)
        inverted_mask = binary_not(combined_mask)
        masked_curve = mask(output_image, inverted_mask)
        update_curve = masked_curve + negative_curve
        
        opening_sphere(update_curve, destination=output_image, radius_x=smoothing, radius_y=smoothing, radius_z=smoothing)

    return output_image


def checkerboard_level_set(image_shape, square_size=5):
    """Create a checkerboard level set with binary values.
    Parameters
    ----------
    image_shape : tuple of positive integers
        Shape of the image.
    square_size : int, optional
        Size of the squares of the checkerboard. It defaults to 5.
    Returns
    -------
    out : array with shape `image_shape`
        Binary level set of the checkerboard.
    See Also
    --------
    disk_level_set
    """

    grid = np.mgrid[[slice(i) for i in image_shape]]
    grid = (grid // square_size)

    # Alternate 0/1 for even/odd numbers.
    grid = grid & 1

    checkerboard = np.bitwise_xor.reduce(grid, axis=0)
    res = np.int8(checkerboard)
    return res