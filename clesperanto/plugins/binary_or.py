from ..core import execute

def binary_or (src1, src2, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src1":src1,
        "src2":src2,
        "dst":dst
    }

    execute(__file__, 'binary_or_' + str(len(dst.shape)) + 'd_x.cl', 'binary_or_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
