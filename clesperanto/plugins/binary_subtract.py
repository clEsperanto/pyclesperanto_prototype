from ..core import execute

def binary_subtract (src1, src2, dst):
    """
    documentation placeholder
    """


    parameters = {
        "dst": dst,
        "src1":src1,
        "src2":src2
    }

    # TODO: Rename cl file and kernel function to fit to naming conventions. This needs to be done in clij2 as well.
    execute(__file__, 'binarySubtract' + str(len(dst.shape)) + 'd_x.cl', 'binary_subtract_image' + str(len(dst.shape)) + 'd', dst.shape, parameters)
