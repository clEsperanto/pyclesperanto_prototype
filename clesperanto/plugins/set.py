from ..core import execute

def set(output, scalar):
    """Sets all pixel values x of a given image X to a constant value v.
    
    <pre>f(x) = v</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, Number value)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_set


    Returns
    -------

    """


    parameters = {
        "dst":output,
        "value":float(scalar)
    }

    execute(__file__, 'set_' + str(len(output.shape)) + 'd_x.cl', 'set_' + str(len(output.shape)) + 'd', output.shape, parameters);
