

from ..core import execute


def dilate_sphere_slice_by_slice (src, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'dilate_sphere_slice_by_slice_' + str(len(dst.shape)) + 'd_x.cl', 'dilate_sphere_slice_by_slice_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

