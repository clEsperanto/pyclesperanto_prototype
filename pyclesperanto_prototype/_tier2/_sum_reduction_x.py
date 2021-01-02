from .._tier0 import execute
from .._tier0 import Image
from .._tier0 import plugin_function
from .._tier0 import create_none

@plugin_function(output_creator=create_none)
def sum_reduction_x(src : Image, dst : Image = None, blocksize : int = 256):
    """Takes an image and reduces it in width by factor blocksize.
    The new pixels contain the sum of the reduced pixels. For example,
    given the following image and block size 4:
    [0, 1, 1, 0, 1, 0, 1, 1]
    would lead to an image
    [2, 3]

    Parameters
    ----------
    src
    dst
    blocksize

    Returns
    -------

    """
    from .._tier0 import create

    if dst is None:
        if len(src.shape) == 3:
            dst = create([src.shape[0], int(src.shape[1], src.shape[2] / blocksize)])
        else: # 2 dimensions
            dst = create([src.shape[0], int(src.shape[1] / blocksize)])

    parameters = {
        "dst": dst,
        "src": src,
        "blocksize": int(blocksize)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/sum_reduction_x_x.cl', 'sum_reduction_x', dst.shape, parameters)

    return dst

