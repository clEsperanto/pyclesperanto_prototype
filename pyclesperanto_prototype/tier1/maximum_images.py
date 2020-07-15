from ..tier0 import execute


def maximum_images (src1, src2, dst):
    """Computes the maximum of a pair of pixel values x, y from two given images X and Y. 
    
    <pre>f(x, y) = max(x, y)</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source1, Image source2, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_maximumImages


    Returns
    -------

    """


    parameters = {
        "src":src1,
        "src1":src2,
        "dst": dst
    }

    execute(__file__, 'maximum_images_' + str(len(dst.shape)) + 'd_x.cl', 'maximum_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

