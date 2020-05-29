from ..core import execute


def multiply_image_and_scalar (src, dst, scalar):

    parameters = {
        "src":src,
        "dst": dst,
        "scalar":float(scalar)
    }

    execute(__file__, 'multiply_image_and_scalar_' + str(len(dst.shape)) + 'd_x.cl', 'multiply_image_and_scalar_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

