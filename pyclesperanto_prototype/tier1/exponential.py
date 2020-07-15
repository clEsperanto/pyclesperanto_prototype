from ..tier0 import execute


def exponential (src, dst):
    """Computes base exponential of all pixels values.
    
    f(x) = exp(x)

    Author(s): Peter Haub, Robert Haase

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_exponential


    Returns
    -------

    """


    parameters = {
        "src":src,
        "dst":dst
    }

    execute(__file__, 'exponential_' + str(len(dst.shape)) + 'd_x.cl', 'exponential_' + str(len(dst.shape)) + 'd', dst.shape, parameters)

