from .._tier0 import execute
from .._tier0 import Image
from .._tier0 import plugin_function

@plugin_function
def block_enumerate(src : Image, src_sums : Image, dst : Image = sum, blocksize : int = 256):
    """Enumerates pixels with value 1 in a one-dimensional image

    For example handing over the image
    [0, 1, 1, 0, 1, 0, 1, 1]
    would be processed to an image
    [0, 1, 2, 0, 3, 0, 4, 5]
    This functionality is important in connected component labeling.

    Processing is accelerated by paralellization in blocks. Therefore,
    handing over pre-computed block sums is neccessary (see also
    sum_reduction_x). In the above example, with blocksize 4, that
    would be the sum array:
    [2, 3]
    Note that the block size when calling this function and sum_reduction
    must be identical

    Parameters
    ----------
    src : Image
        input binary vector image
    src_sums: Image
        pre-computed sums of blocks
    dst : Image
        output enumerated vector image
    blocksize : int
        blocksize; must correspond correctly to how the
        block sums were computed

    Returns
    -------
        dst
    """

    parameters = {
        "dst": dst,
        "src": src,
        "src_sums":src_sums,
        "blocksize": int(blocksize)
    }

    execute(__file__, '../clij-opencl-kernels/kernels/block_enumerate_x.cl', 'block_enumerate', src_sums.shape, parameters)

    return dst