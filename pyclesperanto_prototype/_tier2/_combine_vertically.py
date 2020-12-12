from .._tier0 import plugin_function
from .._tier0 import create
from .._tier0 import create_none
from .._tier0 import Image
from .._tier1 import paste

@plugin_function(output_creator=create_none)
def combine_vertically(source1 : Image, source2 : Image, target : Image = None):
    """

    Parameters
    ----------
    source1
    source2
    target

    Returns
    -------

    """

    import numpy as np
    dimensions = np.asarray(source1.shape)

    if target is None:
        if (len(dimensions) == 3):
            dimensions[1] = dimensions[1] + source2.shape[1]
        else:
            dimensions[0] = dimensions[0] + source2.shape[0]

        target = create(dimensions)

    paste(source1, target, 0, 0, 0)
    paste(source2, target, 0, source1.shape[-2], 0)

    return target
