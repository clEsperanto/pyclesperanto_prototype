from ..tier0 import execute


def draw_box (dst, x, y, z, width, height, depth, value):
    """Draws a box at a given start point with given size. 
    All pixels other than in the box are untouched. Consider using `set(buffer, 0);` in advance.

    Available for: 2D, 3D

    Parameters
    ----------
    (ByRef Image destination, Number x, Number y, Number z, Number width, Number height, Number depth, Number value)
    todo: Better documentation will follow
          In the meantime, read more: https://clij.github.io/clij2-docs/reference_drawBox


    Returns
    -------

    """


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
