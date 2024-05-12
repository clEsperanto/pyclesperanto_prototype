from .._tier0 import plugin_function
from .._tier0 import create
from .._tier0 import create_none
from .._tier0 import Image
from .._tier1 import paste

@plugin_function(output_creator=create_none, categories=['combine', 'transform', 'in assistant'])
def stitch_vertically_linear_blending(image1 : Image, image2 : Image, destination : Image = None, num_pixels_overlap:int=0) -> Image:
    """Combines two images in Y by linearly blending them in an overlapping region.

    Parameters
    ----------
    image1 : Image
    image2 : Image
    destination : Image, optional
    num_pixels_overlap : int, optional

    Returns
    -------
    destination
    """
    from .._tier0 import create, asarray
    from .._tier1 import set_ramp_y, crop
    from .._tier1 import subtract_image_from_scalar
    from .._tier2 import combine_vertically

    num_pixels_overlap = int(num_pixels_overlap)
    image1_width = image1.shape[-1]
    image2_width = image2.shape[-1]
    image1_height = image1.shape[-2]
    image2_height = image2.shape[-2]
    image1_depth = 1 if len(image1.shape) == 2 else image1.shape[-3]
    image2_depth = 1 if len(image2.shape) == 2 else image2.shape[-3]

    # crop out left, right and the two overlapping parts
    top_part = crop(image1, width=image1_width, height=image1_height - num_pixels_overlap, depth=image1_depth)
    center_part1 = crop(image1, start_y=image1_height-num_pixels_overlap, width=image1_width, height=num_pixels_overlap, depth=image1_depth)
    center_part2 = crop(image2, width=image2_width, height=num_pixels_overlap, depth=image2_depth)
    bottom_part = crop(image2, start_y=num_pixels_overlap, width=image2_width, height=image2_height-num_pixels_overlap, depth=image2_depth)

    # setup a gradient for the blending
    gradient = create(center_part1.shape)
    set_ramp_y(gradient)
    gradient_right_left = (gradient + 1) / (gradient.shape[-2]+1)
    gradient_left_right = subtract_image_from_scalar(gradient_right_left, scalar=1)

    # compute the overlapping image by multiplying both images with the gradient
    center_part = asarray(center_part1) * gradient_left_right + asarray(center_part2) * gradient_right_left

    # combine images vertically
    return combine_vertically(combine_vertically(top_part, center_part), bottom_part, destination)
