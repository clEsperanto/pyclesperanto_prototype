from ..core import execute

def set_plane(output, plane, scalar):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "plane":int(plane),
        "value":float(scalar)
    }

    execute(__file__, 'set_plane_' + str(len(output.shape)) + 'd_x.cl', 'set_plane_' + str(len(output.shape)) + 'd', output.shape, parameters);
