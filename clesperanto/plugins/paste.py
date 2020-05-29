from ..core import execute


def paste (src, dst, destination_x, destination_y, destination_z):

    parameters = {
        "dst":dst,
        "src":src,
        "destination_x": int(destination_x),
        "destination_y": int(destination_y)
    }


    if (len(dst.shape) == 3):
        parameters.update({"destination_z": int(destination_z)});

    execute(__file__, 'paste_' + str(len(dst.shape)) + 'd_x.cl', 'paste_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

