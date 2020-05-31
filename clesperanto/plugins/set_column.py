from ..core import execute

def set_column(output, column, scalar):
    parameters = {
        "dst":output,
        "column":int(column),
        "value":float(scalar)
    }

    execute(__file__, 'set_column_' + str(len(output.shape)) + 'd_x.cl', 'set_column_' + str(len(output.shape)) + 'd', output.shape, parameters);
