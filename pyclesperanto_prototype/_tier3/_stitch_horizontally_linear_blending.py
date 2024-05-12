from .._tier0 import plugin_function
from .._tier0 import create
from .._tier0 import create_none
from .._tier0 import Image
from .._tier1 import paste

@plugin_function(output_creator=create_none, categories=['combine', 'transform', 'in assistant'])
def stitch_horizontally_linear_blending(image1 : Image, image2 : Image, destination : Image = None, num_pixels_overlap:int=0) -> Image:
    """Combines two images in X by linearly blending them in an overlapping region.

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
    from .._tier1 import set_ramp_x, crop
    from .._tier1 import subtract_image_from_scalar
    from .._tier2 import combine_horizontally

    num_pixels_overlap = int(num_pixels_overlap)
    image1_width = image1.shape[-1]
    image2_width = image2.shape[-1]
    image1_height = image1.shape[-2]
    image2_height = image2.shape[-2]
    image1_depth = 1 if len(image1.shape) == 2 else image1.shape[-3]
    image2_depth = 1 if len(image2.shape) == 2 else image2.shape[-3]

    # crop out left, right and the two overlapping parts
    left_part = crop(image1, width=image1.shape[-1] - num_pixels_overlap, height=image1_height, depth=image1_depth)
    center_part1 = crop(image1, start_x=image1_width - num_pixels_overlap, width=num_pixels_overlap, height=image1_height, depth=image1_depth)
    center_part2 = crop(image2, width=num_pixels_overlap, height=image2_height, depth=image2_depth)
    right_part = crop(image2, start_x=num_pixels_overlap, width=image2_width - num_pixels_overlap, height=image2_height, depth=image2_depth)

    # setup a gradient for the blending
    gradient = create(center_part1.shape)
    set_ramp_x(gradient)
    gradient_right_left = (gradient + 1) / (gradient.shape[-1]+1)
    gradient_left_right = subtract_image_from_scalar(gradient_right_left, scalar=1)

    # compute the overlapping image by multiplying both images with the gradient
    center_part = asarray(center_part1) * gradient_left_right + asarray(center_part2) * gradient_right_left

    # combine images vertically
    return combine_horizontally(combine_horizontally(left_part, center_part), right_part, destination)
