import numpy as np

from .._tier0 import execute
from .._tier0 import plugin_function
from .._tier0 import Image
import numpy as np

@plugin_function
def nan_to_num(source : Image, destination : Image = None, nan : float = 0, posinf : float = np.nan_to_num(np.inf), neginf : float = np.nan_to_num(-np.inf)) -> Image:
    """Copies all pixels instead those which are not a number (NaN), or positive/negative infinity
    which are replaced by a defined new value, default 0.

    This function aims to work similarly as its counterpart in numpy [1].
    Default values for posinf and neginf may differ from numpy and even differ depending on compute hardware.
    It is recommended to specify those values.

    Parameters
    ----------
    source : Image
    destination : Image, optional
    nan: float, optional
        default 0
    posinf: float, optional
        default: a very large number
    neginf: float, optional
        default a very small number

    Returns
    -------
    destination
    
    See also
    --------
    ..[1] https://numpy.org/doc/stable/reference/generated/numpy.nan_to_num.html
    """
    print("posinf", float(posinf))
    print("neginf", neginf)

    parameters = {
        "dst":destination,
        "src":source,
        "new_nan_value":float(nan),
        "new_posinf_value":float(posinf),
        "new_neginf_value":float(neginf),
    }

    execute(__file__, 'nan_to_num.cl', 'nan_to_num', destination.shape, parameters)
    return destination
