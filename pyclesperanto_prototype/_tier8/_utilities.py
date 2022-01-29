import warnings
import math
import numpy as np

def transform_from_string(text: str, image: np.ndarray):
    """
    Turns a string containing a description of an affine transform into a AffineTransform3D object

    Parameters
    ----------
    text: str
    image: Image
        The image to be transformed. Should have a shape.

    Returns
    -------
    AffineTransform3D
    """
    # Translated from https://github.com/clij/clij2/blob/a13ebc54863d56c5866e4343844764e5cc63cb0c/src/main/java/net/haesleinhuepf/clij2/plugins/AffineTransform3D.java#L50
    from ._AffineTransform3D import AffineTransform3D
    at = AffineTransform3D()
    while " =" in text:
        text = text.replace(" =", "=")
    while "= " in text:
        text = text.replace("= ", "=")
    for transform_command in text.split(" "):
        command_parts = transform_command.split("=")

        try:
            number = float(command_parts[1])
        except:
            number = 0

        if command_parts[0] == "center":
            at.center(image.shape)
        elif command_parts[0] == "-center":
            at.center(image.shape, undo=True)
        elif command_parts[0] == "scale":
            at.scale(scale_x=number, scale_y=number, scale_z=number)
        elif command_parts[0] == "scalex" or command_parts[0] == "scale_x":
            at.scale(scale_x=number)
        elif command_parts[0] == "scaley" or command_parts[0] == "scale_y":
            at.scale(scale_y=number)
        elif command_parts[0] == "scalez" or command_parts[0] == "scale_z":
            at.scale(scale_z=number)
        elif command_parts[0] == "rotatex" or command_parts[0] == "rotate_x":
            at.rotate(axis=0, angle_in_degrees=number)
        elif command_parts[0] == "rotatey" or command_parts[0] == "rotate_y":
            at.rotate(axis=1, angle_in_degrees=number)
        elif command_parts[0] == "rotatez" or command_parts[0] == "rotate_z" or command_parts[0] == "rotate":
            at.rotate(axis=2, angle_in_degrees=number)
        elif command_parts[0] == "translatex" or command_parts[0] == "translate_x":
            at.translate(translate_x=number)
        elif command_parts[0] == "translatey" or command_parts[0] == "translate_y":
            at.translate(translate_y=number)
        elif command_parts[0] == "translatez" or command_parts[0] == "translate_z":
            at.translate(translate_z=number)
        elif command_parts[0] == "shearxy":
            at.shear_in_z_plane(angle_x_in_degrees=-shear_factor_to_shear_angle(number))
        elif command_parts[0] == "shearxz":
            at.shear_in_y_plane(angle_x_in_degrees=-shear_factor_to_shear_angle(number))
        elif command_parts[0] == "shearyx":
            at.shear_in_z_plane(angle_y_in_degrees=-shear_factor_to_shear_angle(number))
        elif command_parts[0] == "shearyz":
            at.shear_in_x_plane(angle_y_in_degrees=-shear_factor_to_shear_angle(number))
        elif command_parts[0] == "shearzx":
            at.shear_in_y_plane(angle_z_in_degrees=-shear_factor_to_shear_angle(number))
        elif command_parts[0] == "shearzy":
            at.shear_in_x_plane(angle_z_in_degrees=-shear_factor_to_shear_angle(number))
        elif command_parts[0] == "shear_in_x_plane_along_y":
            at.shear_in_x_plane(angle_y_in_degrees=number)
        elif command_parts[0] == "shear_in_x_plane_along_z":
            at.shear_in_x_plane(angle_z_in_degrees=number)
        elif command_parts[0] == "shear_in_y_plane_along_x":
            at.shear_in_y_plane(angle_x_in_degrees=number)
        elif command_parts[0] == "shear_in_y_plane_along_z":
            at.shear_in_y_plane(angle_z_in_degrees=number)
        elif command_parts[0] == "shear_in_z_plane_along_x":
            at.shear_in_z_plane(angle_x_in_degrees=number)
        elif command_parts[0] == "shear_in_z_plane_along_y":
            at.shear_in_z_plane(angle_y_in_degrees=number)
        else:
            warnings.warn("Unknown transform:" + str(command_parts[0]))

    return at


def shear_angle_to_shear_factor(angle_in_degrees):
    """
    Converts a shearing angle into a shearing factor

    Parameters
    ----------
    angle_in_degrees: float

    Returns
    -------
    float
    """
    return 1.0 / math.tan((90 - angle_in_degrees) * math.pi / 180)

def shear_factor_to_shear_angle(shear_factor):
    """
    Converts a shearing angle into a shearing factor

    Parameters
    ----------
    shear_factor: float

    Returns
    -------
    float
    """
    return  - math.atan(1.0 / shear_factor) * 180 / math.pi + 90