from .._tier0 import execute


def block_enumerate(src, src_sums, dst, blocksize):
    """
    docs
    """

    parameters = {
        "dst": dst,
        "src": src,
        "src_sums":src_sums,
        "blocksize": int(blocksize)
    }

    execute(__file__, 'block_enumerate.cl', 'block_enumerate', src_sums.shape, parameters)

