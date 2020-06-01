

from ..core import execute


def dilate_box (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'dilate_box_' + str(len(dst.shape)) + 'd_x.cl', 'dilate_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

