from .._tier0 import execute


def multiply_images (src1, src2, dst):
    """Multiplies all pairs of pixel values x and y from two image X and Y.
    
    <pre>f(x, y) = x * y</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image factor1, Image factor2, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_multiplyImages


    Returns
    -------

    """


    parameters = {
        "src":src1,
        "src1":src2,
        "dst": dst
    }

    execute(__file__, 'multiply_images_' + str(len(dst.shape)) + 'd_x.cl', 'multiply_images_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

