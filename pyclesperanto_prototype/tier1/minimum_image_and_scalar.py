from ..tier0 import execute


def minimum_image_and_scalar (src, dst, scalar):
    """Computes the minimum of a constant scalar s and each pixel value x in a given image X.
    
    <pre>f(x, s) = min(x, s)</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number scalar)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_minimumImageAndScalar


    Returns
    -------

    """


    parameters = {
        "src":src,
        "dst": dst,
        "valueB":float(scalar)
    }

    execute(__file__, 'minimum_image_and_scalar_' + str(len(dst.shape)) + 'd_x.cl', 'minimum_image_and_scalar_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

