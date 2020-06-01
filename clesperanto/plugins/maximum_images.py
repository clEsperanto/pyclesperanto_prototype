from ..core import execute


def maximum_images (src1, src2, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src1,
        "src1":src2,
        "dst": dst
    }

    execute(__file__, 'maximum_images_' + str(len(dst.shape)) + 'd_x.cl', 'maximum_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

