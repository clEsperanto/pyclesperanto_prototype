from pyclesperanto_prototype._tier0 import plugin_function
from pyclesperanto_prototype._tier0 import Image
def standard_deviation_box(source: Image, destination: Image = None, radius_x : int = 1, radius_y : int = 1, radius_z : int = 1):
    """Computes the local standard deviation of a pixels box neighborhood. The box size is specified by
    its half-width, half-height and half-depth (radius). If 2D images are given, radius_z will be ignored.

    Parameters
    ----------
    source : Image
    destination : Image
    radius_x : int
    radius_y : int
    radius_z : int

    Returns
    -------
    destination

    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.standard_deviation_box(source, destination, 10, 10, 10)

    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_standardDeviationBox
    """

    from .._tier1 import variance_box, power

    temp = variance_box(source, radius_x=radius_x, radius_y=radius_y, radius_z=radius_z)

    return power(temp, destination, exponent=0.5)

