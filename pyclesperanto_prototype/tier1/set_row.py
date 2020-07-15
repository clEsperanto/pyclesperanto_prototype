from ..tier0 import execute

def set_row(output, row, scalar):
    """Sets all pixel values x of a given row in X to a constant value v.
    
    <pre>f(x) = v</pre>

    Available for: 2D, 3D

    Parameters
    ----------
    (Image source, Number rowIndex, Number value)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_setRow


    Returns
    -------

    """


    parameters = {
        "dst":output,
        "row":int(row),
        "value":float(scalar)
    }

    execute(__file__, 'set_row_' + str(len(output.shape)) + 'd_x.cl', 'set_row_' + str(len(output.shape)) + 'd', output.shape, parameters);
