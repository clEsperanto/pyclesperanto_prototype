from ..core import execute


def maximum_image_and_scalar (src, dst, scalar):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "dst": dst,
        "valueB":float(scalar)
    }

    execute(__file__, 'maximum_image_and_scalar_' + str(len(dst.shape)) + 'd_x.cl', 'maximum_image_and_scalar_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

