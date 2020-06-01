from ..core import execute

def set_row(output, row, scalar):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "row":int(row),
        "value":float(scalar)
    }

    execute(__file__, 'set_row_' + str(len(output.shape)) + 'd_x.cl', 'set_row_' + str(len(output.shape)) + 'd', output.shape, parameters);
