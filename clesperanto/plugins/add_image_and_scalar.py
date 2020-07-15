from ..core import execute


def add_image_and_scalar(input, output, scalar):
    """Adds a scalar value s to all pixels x of a given image X.
    
    <pre>f(x, s) = x + s</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, ByRef Image destination, Number scalar)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_addImageAndScalar


    Returns
    -------

    """

    parameters = {"src": input, "dst": output, "scalar": float(scalar)}
    execute("add_image_and_scalar", output.shape, parameters)
