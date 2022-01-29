from .._tier0 import execute

from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function
def hessian_eigenvalues(source: Image,
                        small_eigenvalue_destination: Image = None,
                        middle_eigenvalue_destination: Image = None,
                        large_eigenvalue_destination: Image = None,
                        ) -> Image:
    """Computes the eigenvalues of the hessian matrix of a 2d or 3d image.

    Hessian matrix or 2D images:
      [Ixx, Ixy]
      [Ixy, Iyy]

    Hessian matrix for 3D images:
      [Ixx, Ixy, Ixz]
      [Ixy, Iyy, Iyz]
      [Ixz, Iyz, Izz]

    Ixx denotes the second derivative in x.

    Ixx and Iyy are calculated by convolving the image with the 1d kernel [1 -2 1].
    Ixy is calculated by a convolution with the 2d kernel:
      [ 0.25 0 -0.25]
      [    0 0     0]
      [-0.25 0  0.25]

    Note: This is the only clesperanto function that returns multiple images. This API might be
    subject to change in the future. Consider using small_hessian_eigenvalue() and/or large_hessian_eigenvalue()
    instead which return only one image.

    Parameters
    ----------
    source: Image
    small_eigenvalue_destination: Image, optional
    middle_eigenvalue_destination: Image, optional
    large_eigenvalue_destination: Image, optional

    Returns
    -------
    small_eigenvalue_destination: Image
    middle_eigenvalue_destination: Image
    large_eigenvalue_destination: Image

    """
    if len(source.shape) == 2:
        parameters = {
            "src": source,
            "small_eigenvalue": small_eigenvalue_destination,
            "large_eigenvalue": large_eigenvalue_destination,
        }
    else:  # 3D
        parameters = {
            "src": source,
            "small_eigenvalue": small_eigenvalue_destination,
            "middle_eigenvalue": middle_eigenvalue_destination,
            "large_eigenvalue": large_eigenvalue_destination,
        }

    execute(__file__, 'hessian_eigenvalues_' + str(len(source.shape)) + 'd.cl', 'hessian_eigenvalues_' + str(len(source.shape)) + 'd', source.shape, parameters)

    if len(source.shape) == 2:
        return small_eigenvalue_destination, None, large_eigenvalue_destination
    else:  # 3D
        return small_eigenvalue_destination, middle_eigenvalue_destination, large_eigenvalue_destination
