from ..core import execute

def convolve (src, kernelImage, dst):
    """
    documentation placeholder
    """


    parameters = {
        "src":src,
        "kernelImage":kernelImage,
        "dst":dst
    }

    execute(__file__, 'convolve_' + str(len(dst.shape)) + 'd_x.cl', 'convolve_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
