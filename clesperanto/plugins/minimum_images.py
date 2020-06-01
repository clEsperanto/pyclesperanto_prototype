from ..core import execute


def minimum_images (src1, src2, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src1,
        "src1":src2,
        "dst": dst
    }

    execute(__file__, 'minimum_images_' + str(len(dst.shape)) + 'd_x.cl', 'minimum_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

