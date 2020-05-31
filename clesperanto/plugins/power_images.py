from ..core import execute


def power_images (src1, src2, dst):

    parameters = {
        "dst": dst,
        "src1":src1,
        "src2":src2
    }

    execute(__file__, 'power_images_' + str(len(dst.shape)) + 'd_x.cl', 'power_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

