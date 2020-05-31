from ..core import execute


def replace_intensities(src, map, dst):

    parameters = {
        "dst": dst,
        "src": src,
        "map": map
    }

    execute(__file__, 'replace_intensities_x.cl', 'replace_intensities', dst.shape, parameters)

