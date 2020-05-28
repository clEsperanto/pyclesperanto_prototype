

from ..core import execute


def dilate_box_slice_by_slice (src, dst):

    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'dilate_box_slice_by_slice_' + str(len(dst.shape)) + 'd_x.cl', 'dilate_box_slice_by_slice_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

