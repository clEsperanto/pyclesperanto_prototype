

from ..core import execute


def erode_box (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'erode_box_' + str(len(dst.shape)) + 'd_x.cl', 'erode_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

