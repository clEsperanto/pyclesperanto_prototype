from .._tier0 import execute


def copy (src, dst):
    """Copies an image.
    
    <pre>f(x) = x</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_copy


    Returns
    -------

    """


    parameters = {
        "dst":dst,
        "src":src
    }

    execute(__file__, 'copy_' + str(len(dst.shape)) + 'd_x.cl', 'copy_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
