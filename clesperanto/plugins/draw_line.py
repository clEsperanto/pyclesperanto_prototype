from ..core import execute


def draw_line (dst, x1, y1, z1, x2, y2, z2, thickness, value):
    """
    documentation placeholder
    """


    if (len(dst.shape) == 2):
        parameters = {
            "dst": dst,
            "x1": float(x1),
            "y1": float(y1),
            "x2": float(x2),
            "y2": float(y2),
            "radius": float(thickness),
            "value": float(value)
        }
    else: # 3D
        parameters = {
            "dst": dst,
            "x1": float(x1),
            "y1": float(y1),
            "z1": float(z1),
            "x2": float(x2),
            "y2": float(y2),
            "z2": float(z2),
            "radius": float(thickness),
            "value": float(value)
        }

    # todo: rename cl file (missing _ between drawn and line)
    # todo: rname kernel name (upper case D should be lower case d)

    execute(__file__, 'drawline_' + str(len(dst.shape)) + 'd_x.cl', 'draw_line_' + str(len(dst.shape)) + 'D', dst.shape, parameters)
