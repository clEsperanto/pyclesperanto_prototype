from ..core import execute


def draw_box (dst, x, y, z, width, height, depth, value):
    if (len(dst.shape) == 2):
        parameters = {
            "dst": dst,
            "x1": float(x),
            "y1": float(y),
            "x2": float(x + width),
            "y2": float(y + height),
            "value": float(value)
        }
    else: # 3D
        parameters = {
            "dst": dst,
            "x1": float(x),
            "y1": float(y),
            "z1": float(z),
            "x2": float(x + width),
            "y2": float(y + height),
            "z2": float(z + depth),
            "value": float(value)
        }

    execute(__file__, 'draw_box_' + str(len(dst.shape)) + 'd_x.cl', 'draw_box_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
