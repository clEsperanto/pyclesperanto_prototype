

from ..core import execute


def erode_sphere (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'erode_sphere_' + str(len(dst.shape)) + 'd_x.cl', 'erode_sphere_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

