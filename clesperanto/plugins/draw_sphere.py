from ..core import execute


def draw_sphere (dst, x, y, z, radius_x, radius_y, radius_z, value):
    if (len(dst.shape) == 2):
        parameters = {
            "dst": dst,
            "cx": float(x),
            "cy": float(y),
            "rx": float(radius_x),
            "ry": float(radius_y),
            "rxsq": float(radius_x * radius_x),
            "rysq": float(radius_y * radius_y),
            "value": float(value)
        }
    else: # 3D
        parameters = {
            "dst": dst,
            "cx": float(x),
            "cy": float(y),
            "cz": float(z),
            "rx": float(radius_x),
            "ry": float(radius_y),
            "rz": float(radius_z),
            "rxsq": float(radius_x * radius_x),
            "rysq": float(radius_y * radius_y),
            "rzsq": float(radius_z * radius_z),
            "value": float(value)
        }

    execute(__file__, 'draw_sphere_' + str(len(dst.shape)) + 'd_x.cl', 'draw_sphere_' + str(len(dst.shape)) + 'd', dst.shape, parameters)
