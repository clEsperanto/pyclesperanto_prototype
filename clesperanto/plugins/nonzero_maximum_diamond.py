from ..core import execute

def nonzero_maximum_diamond (src, flag_dst, dst):

    parameters = {
        "dst": dst,
        "flag_dst": flag_dst,
        "src":src,
    }

    execute(__file__, 'nonzero_maximum_diamond_' + str(len(dst.shape)) + 'd_x.cl', 'nonzero_maximum_diamond_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return [flag_dst, dst]
