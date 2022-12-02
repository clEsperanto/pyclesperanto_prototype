from .._tier0 import plugin_function, create, create_none, Image

@plugin_function(output_creator=create_none)
def crop_border(input_image:Image, destination_image:Image = None, border_size: int = 1) -> Image:
    """Crops an image by removing the outer pixels, per default 1.

    Notes
    -----
    * To make sure the output image has the right size, provide destination_image=None.

    Parameters
    ----------
    input_image: Image
    destination_image: Image
    border_size: int

    Returns
    -------
    destination_image
    """
    if destination_image is None:
        if len(input_image.shape) == 2:
            destination_image = create((input_image.shape[0]-2, input_image.shape[1]-2), input_image.dtype)
        else:
            destination_image = create((input_image.shape[0] - 2, input_image.shape[1] - 2, input_image.shape[2] - 2), input_image.dtype)

    from .._tier1 import crop

    if len(input_image.shape) == 2:
        crop(input_image,
             destination_image,
             start_x=border_size,
             start_y=border_size,
             height=input_image.shape[0] - border_size * 2,
             width=input_image.shape[1] - border_size * 2)
    else:
        crop(input_image,
                  destination_image,
                      start_x=border_size,
                      start_y=border_size,
                      start_z=border_size,
                      depth=input_image.shape[0] - border_size*2,
                      height=input_image.shape[1] - border_size*2,
                      width=input_image.shape[2] - border_size*2)

    return destination_image