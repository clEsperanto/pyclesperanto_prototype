from ..core import execute

def onlyzero_overwrite_maximum_diamond (src, flag_dst, dst):
    """
    documentation placeholder
    """


    parameters = {
        "dst": dst,
        "flag_dst": flag_dst,
        "src":src,
    }

    execute(__file__, 'onlyzero_overwrite_maximum_diamond_' + str(len(dst.shape)) + 'd_x.cl', 'onlyzero_overwrite_maximum_diamond_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

    return [flag_dst, dst]
