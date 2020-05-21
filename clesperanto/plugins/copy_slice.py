from ..core import execute


def copy_slice (src, dst, slice):

    parameters = {
        "dst":dst,
        "src":src,
        "slice":int(slice)
    }

    if (len(dst.shape) == 3):
        execute(__file__, 'copy_slice_to_3d_x.cl', 'copy_slice_to_3d', dst.shape, parameters)
    else:
        execute(__file__, 'copy_slice_from_3d_x.cl', 'copy_slice_from_3d', dst.shape, parameters)

