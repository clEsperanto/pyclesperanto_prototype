from ..core import execute


def power (src, dst, exponent):
    """Computes all pixels value x to the power of a given exponent a.
    
    <pre>f(x, a) = x ^ a</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number exponent)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_power


    Returns
    -------

    """


    parameters = {
        "src":src,
        "dst": dst,
        "exponent":float(exponent)
    }

    execute(__file__, 'power_' + str(len(dst.shape)) + 'd_x.cl', 'power_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

