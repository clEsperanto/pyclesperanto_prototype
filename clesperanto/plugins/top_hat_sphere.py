from ..core import create
from ..plugins import minimum_sphere
from ..plugins import maximum_sphere
from ..plugins import add_images_weighted


def top_hat_sphere(input, output, radius_x, radius_y, radius_z=0):
    temp1 = create(input.shape);
    temp2 = create(input.shape);

    minimum_sphere(input, temp1, radius_x, radius_y, radius_z);
    maximum_sphere(temp1, temp2, radius_x, radius_y, radius_z);
    add_images_weighted(input, temp2, output, 1, -1);