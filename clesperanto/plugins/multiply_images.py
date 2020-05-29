from ..core import execute


def multiply_images (src1, src2, dst):

    parameters = {
        "src":src1,
        "src1":src2,
        "dst": dst
    }

    execute(__file__, 'multiply_images_' + str(len(dst.shape)) + 'd_x.cl', 'multiply_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

