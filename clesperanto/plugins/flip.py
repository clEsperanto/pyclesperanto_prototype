from ..core import execute

def flip (src, dst, flip_x, flip_y, flip_z):

    parameters = {
        "src":src,
        "dst":dst,
        "flipx": int(1 if flip_x else 0),
        "flipy": int(1 if flip_y else 0)
    }

    if (len(dst.shape) == 3):
        parameters.update({"flipz": int(1 if flip_z else 0)});

    execute(__file__, 'flip_' + str(len(dst.shape)) + 'd_x.cl', 'flip_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

