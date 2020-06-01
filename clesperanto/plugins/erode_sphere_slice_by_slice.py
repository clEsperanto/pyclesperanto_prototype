

from ..core import execute


def erode_sphere_slice_by_slice (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'erode_sphere_slice_by_slice_' + str(len(dst.shape)) + 'd_x.cl', 'erode_sphere_slice_by_slice_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

