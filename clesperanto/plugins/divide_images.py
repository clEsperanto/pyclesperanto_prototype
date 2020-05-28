from ..core import execute


def divide_images (src, src1, dst):

    parameters = {
        "src":src,
        "src1":src1,
        "dst":dst
    }

    execute(__file__, 'divide_images_' + str(len(dst.shape)) + 'd_x.cl', 'divide_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

