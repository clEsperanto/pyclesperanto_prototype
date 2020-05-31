from ..core import execute

def nonzero_minimum_diamond (src, flag_dst, dst):

    parameters = {
        "dst": dst,
        "flag_dst": flag_dst,
        "src":src,
    }

    execute(__file__, 'nonzero_minimum_diamond_' + str(len(dst.shape)) + 'd_x.cl', 'nonzero_minimum_diamond_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return [flag_dst, dst]
