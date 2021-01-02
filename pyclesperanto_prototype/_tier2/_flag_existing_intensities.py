from .._tier0 import execute
from .._tier1 import set

def flag_existing_intensities(src, dst):
    """
    docs
    """

    parameters = {
        "dst": dst,
        "src": src
    }

    set(dst, 0)

    execute(__file__, '../clij-opencl-kernels/kernels/flag_existing_intensities_x.cl', 'flag_existing_intensities', src.shape, parameters)

