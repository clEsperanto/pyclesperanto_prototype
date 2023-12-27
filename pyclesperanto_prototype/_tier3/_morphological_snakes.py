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
from .._tier1 import gradient_z, copy, power
from .._tier1 import greater_constant, smaller_constant
from .._tier1 import mask, add_image_and_scalar, add_images_weighted
from .._tier2 import opening_sphere, closing_sphere

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

    temp_1 = create_like(output_image)
    temp_2 = create_like(output_image)
    temp_3 = create_like(output_image)
    temp_4 = create_like(output_image)
    temp_5 = create_like(output_image)

    for _ in range(n_iter):

        # c0 = (image * (1 - u)).sum() / float((1 - u).sum() + 1e-8)
        # c1 = (image * u).sum() / float(u.sum() + 1e-8)

        # define invert image
        binary_not(output_image, destination=temp_1)

        # compute outside contour score
        sum_image_value = mask(input_image, mask=temp_1).sum()
        sum_contour_value = temp_1.sum() + 1e-8
        c0 = - (sum_image_value / sum_contour_value)

        # compute inside contour score
        sum_image_value = mask(input_image, mask=output_image).sum()
        sum_contour_value = output_image.sum() + 1e-8
        c1 = - (sum_image_value / sum_contour_value)


        # du = np.gradient(u)
        # abs_du = np.abs(du).sum(0)
        
        # compute gradient on contour in all direction
        for d in range(input_image.ndim):
            if d == 0:   
                gradient_x(output_image, destination=temp_1)
                absolute(temp_1, destination=temp_2)
                temp_3 += temp_2
            if d == 1:
                gradient_y(output_image, destination=temp_1)
                absolute(temp_1, destination=temp_2)
                temp_3 += temp_2
            if d == 2:
                gradient_z(output_image, destination=temp_1)
                absolute(temp_1, destination=temp_2)
                temp_3 += temp_2

        # compute contour evolution according to gradient and score on contour

        # aux = abs_du * (lambda1 * (image - c1)**2 - lambda2 * (image - c0)**2)


        add_image_and_scalar(input_image, destination=temp_1, scalar=c1)
        add_image_and_scalar(input_image, destination=temp_2, scalar=c0)
        power(temp_1, destination=temp_4, exponent=2)
        power(temp_2, destination=temp_5, exponent=2)
        temp_2 = temp_3 * (lambda1 * temp_4 - lambda2 * temp_5)

        # apply contour update on contour image

        # u[aux < 0] = 1
        # u[aux > 0] = 0

        # # Smoothing
        # for _ in range(smoothing):
        #     u = _curvop(u)



        greater_constant(temp_2, destination=temp_1, constant=0)
        smaller_constant(temp_2, destination=temp_3, constant=0)

        binary_or(temp_1, temp_3, destination=temp_4)
        binary_not(temp_4, destination=temp_1)
        mask(output_image, mask=temp_1, destination=temp_2)
        add_images_weighted(temp_2, temp_3, destination=temp_1, factor1=1, factor2=1)
        
        # smooth contour
        for _ in range(smoothing):
            opening_sphere(temp_1, destination=temp_2, radius_x=1, radius_y=1, radius_z=1)
            closing_sphere(temp_2, destination=temp_1, radius_x=1, radius_y=1, radius_z=1)
        
        copy(temp_1, destination=output_image)

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