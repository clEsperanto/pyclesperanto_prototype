from ..core import execute

def nonzero_maximum_box (src, flag_dst, dst):
    """
    documentation placeholder
    """


    parameters = {
        "dst": dst,
        "flag_dst": flag_dst,
        "src":src,
    }

    execute(__file__, 'nonzero_maximum_box_' + str(len(dst.shape)) + 'd_x.cl', 'nonzero_maximum_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return [flag_dst, dst]
