from ..core import execute


def replace_intensity(src, dst, value_to_replace, value_replacement):

    parameters = {
        "dst": dst,
        "src":src,
        "in":float(value_to_replace),
        "out":float(value_replacement)
    }

    execute(__file__, 'replace_intensity_x.cl', 'replace_intensity', dst.shape, parameters)

