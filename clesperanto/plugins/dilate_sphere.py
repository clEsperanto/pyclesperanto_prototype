

from ..core import execute


def dilate_sphere (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'dilate_sphere_' + str(len(dst.shape)) + 'd_x.cl', 'dilate_sphere_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

