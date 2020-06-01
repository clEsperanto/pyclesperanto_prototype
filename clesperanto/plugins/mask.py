from ..core import execute


def mask (src, mask, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "mask":mask,
        "dst":dst
    }

    execute(__file__, 'mask_' + str(len(dst.shape)) + 'd_x.cl', 'mask_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

