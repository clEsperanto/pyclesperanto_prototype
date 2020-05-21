from ..core import execute


def copy (src, dst):

    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'copy_' + str(len(dst.shape)) + 'd_x.cl', 'copy_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
