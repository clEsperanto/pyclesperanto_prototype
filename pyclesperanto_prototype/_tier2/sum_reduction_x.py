from .._tier0 import execute


def sum_reduction_x(src, dst, blocksize):
    """
    docs
    """

    parameters = {
        "dst": dst,
        "src": src,
        "blocksize": int(blocksize)
    }

    execute(__file__, 'sum_reduction_x.cl', 'sum_reduction_x', dst.shape, parameters)

