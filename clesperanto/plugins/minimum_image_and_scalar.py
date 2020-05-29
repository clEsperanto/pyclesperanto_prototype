from ..core import execute


def minimum_image_and_scalar (src, dst, scalar):

    parameters = {
        "src":src,
        "dst": dst,
        "valueB":float(scalar)
    }

    execute(__file__, 'minimum_image_and_scalar_' + str(len(dst.shape)) + 'd_x.cl', 'minimum_image_and_scalar_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

