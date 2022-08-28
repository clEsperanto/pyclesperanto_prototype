from .._tier0 import plugin_function
from .._tier0 import Image, create_none

@plugin_function(output_creator=create_none)
def prefix_in_x(source:Image, destination:Image = None, scalar:float=0):
    """Takes a matrix or vector and adds a scalar in x-direction.

    This is often useful, e.g. if you have a vector of measurements and you need a vector of background 0 and behind
    measurements.

    input: 1, 3, 4
    output: 0, 1, 3, 4

    Parameters
    ----------
    source: Image
    destination: Image, optional
    scalar: float, optional

    Returns
    -------
    destination
    """
    from .._tier0 import create
    from .._tier1 import paste, set_column

    shape = list(source.shape)
    shape[-1] = shape[-1] + 1

    if destination is None:
        destination = create(shape, dtype=source.dtype)

    set_column(destination, value=scalar)
    return paste(source, destination, destination_x=1)
