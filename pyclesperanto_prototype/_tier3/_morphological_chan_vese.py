import numpy as np
from .._tier0 import Image, plugin_function

@plugin_function
def morphological_chan_vese(input_image: Image,
                            contour_image : Image = np.zeros((0, 0)),
                            output_image : Image = None,
                            num_iter : int = 100,
                            smoothing : int = 1,
                            lambda1 : float = 1,
                            lambda2 : float = 1) -> Image:
    """Morphological Active Contours without Edges (MorphACWE)

    Active contours without edges implemented with morphological operators. It
    can be used to segment objects in images and volumes without well defined
    borders. It is required that the inside of the object looks different on
    average than the outside (i.e., the inner area of the object should be
    darker or lighter than the outer area on average).

    This is a re-implementation of the algorithm in scikit-image [2].

    Parameters
    ----------
    input_image: Image
    contour_image: Image, optional
    output_image: Image, optional
    num_iter : uint
        Number of iterations to run
    smoothing: int, optional
    lambda1 : float, optional
        Weight parameter for the outer region. If `lambda1` is larger than
        `lambda2`, the outer region will contain a larger range of values than
        the inner region.
    lambda2 : float, optional
        Weight parameter for the inner region. If `lambda2` is larger than
        `lambda1`, the inner region will contain a larger range of values than
        the outer region.

    Returns
    -------
    Final segmentation

    Notes
    -----
    This is a version of the Chan-Vese algorithm that uses morphological
    operators instead of solving a partial differential equation (PDE) for the
    evolution of the contour. The set of morphological operators used in this
    algorithm are proved to be infinitesimally equivalent to the Chan-Vese PDE
    (see [1]_). However, morphological operators are do not suffer from the
    numerical stability issues typically found in PDEs (it is not necessary to
    find the right time step for the evolution), and are computationally
    faster.

    The algorithm and its theoretical derivation are described in [1]_.

    References
    ----------
    .. [1] A Morphological Approach to Curvature-based Evolution of Curves and
           Surfaces, Pablo Márquez-Neila, Luis Baumela, Luis Álvarez. In IEEE
           Transactions on Pattern Analysis and Machine Intelligence (PAMI),
           2014, :DOI:`10.1109/TPAMI.2013.106`
    .. [2] https://github.com/scikit-image/scikit-image/blob/5e74a4a3a5149a8a14566b81a32bb15499aa3857/skimage/segmentation/morphsnakes.py#L212-L312
    """
    from .._tier0 import create_like
    from .._tier1 import superior_inferior, inferior_superior, set

    from .._tier1 import absolute, binary_or, binary_not, gradient_x, gradient_y
    from .._tier1 import gradient_z, copy, power
    from .._tier1 import greater_constant, smaller_constant
    from .._tier1 import mask, add_image_and_scalar, add_images_weighted

    if contour_image.size == 0:
        contour_image = checkerboard_level_set(input_image.shape)
    
    greater_constant(contour_image, destination=output_image, constant=0)

    temp_1 = create_like(output_image)
    temp_2 = create_like(output_image)
    temp_3 = create_like(output_image)
    temp_4 = create_like(output_image)
    temp_5 = create_like(output_image)

    for _ in range(num_iter):
        set(temp_3, 0)

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

        # Image attachment
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
        add_image_and_scalar(input_image, destination=temp_1, scalar=c1)
        add_image_and_scalar(input_image, destination=temp_2, scalar=c0)
        power(temp_1, destination=temp_4, exponent=2)
        power(temp_2, destination=temp_5, exponent=2)
        temp_2 = temp_3 * (lambda1 * temp_4 - lambda2 * temp_5)

        # apply contour update on contour image
        greater_constant(temp_2, destination=temp_1, constant=0)
        smaller_constant(temp_2, destination=temp_3, constant=0)

        binary_or(temp_1, temp_3, destination=temp_4)
        binary_not(temp_4, destination=temp_1)
        mask(output_image, mask=temp_1, destination=temp_2)
        add_images_weighted(temp_2, temp_3, destination=temp_1, factor1=1, factor2=1)

        # smooth contour
        for s in range(smoothing):
            if s % 2 == 0:
                inferior_superior(temp_1, temp_2)
                superior_inferior(temp_2, temp_1)
            else:
                superior_inferior(temp_1, temp_2)
                inferior_superior(temp_2, temp_1)
        
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