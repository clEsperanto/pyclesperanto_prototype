from ..tier0 import execute


def maximum_image_and_scalar (src, dst, scalar):
    """Computes the maximum of a constant scalar s and each pixel value x in a given image X. 
    
    <pre>f(x, s) = max(x, s)</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number scalar)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_maximumImageAndScalar


    Returns
    -------

    """


    parameters = {
        "src":src,
        "dst": dst,
        "valueB":float(scalar)
    }

    execute(__file__, 'maximum_image_and_scalar_' + str(len(dst.shape)) + 'd_x.cl', 'maximum_image_and_scalar_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

