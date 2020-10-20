from .._tier0 import Image
from .._tier0 import create_2d_xy
from .._tier0 import execute
from .._tier1 import transpose_xz
from .._tier0 import pull

def __minimum_of_masked_pixels_reduction(input : Image, input_mask : Image, output : Image, output_mask : Image):
    parameters = {
        "dst_min": output,
        "dst_mask": output_mask,
        "mask": input_mask,
        "src": input
    }

    execute(__file__, 'minimum_of_masked_pixels_3d_2d_x.cl', 'minimum_of_masked_pixels_3d_2d', output.shape,
            parameters)


def minimum_of_masked_pixels(input : Image, mask : Image):

    dimensionality = input.shape

    if (len(dimensionality) == 3): # 3D image
        reduced_image = create_2d_xy(input)
        reduced_mask = create_2d_xy(mask)

        __minimum_of_masked_pixels_reduction(input, mask, reduced_image, reduced_mask)

        input = reduced_image
        mask = reduced_mask

    if (len(dimensionality) == 2): # 2D image
        temp_input = transpose_xz(input)
        temp_mask = transpose_xz(mask)
        reduced_image = create_2d_xy(temp_input)
        reduced_mask = create_2d_xy(temp_mask)

        __minimum_of_masked_pixels_reduction(temp_input, temp_mask, reduced_image, reduced_mask)

        input = reduced_image
        mask = reduced_mask

    temp_input = transpose_xz(input)
    temp_mask = transpose_xz(mask)
    reduced_image = create_2d_xy(temp_input)
    reduced_mask = create_2d_xy(temp_mask)

    __minimum_of_masked_pixels_reduction(temp_input, temp_mask, reduced_image, reduced_mask)

    return pull(reduced_image)[0]

