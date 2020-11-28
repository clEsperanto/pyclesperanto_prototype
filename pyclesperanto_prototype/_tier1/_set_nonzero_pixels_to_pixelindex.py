from .._tier0 import execute

def set_nonzero_pixels_to_pixelindex(input, output, offset=1):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "src":input,
        "offset":int(offset)
    }

    execute(__file__, 'set_nonzero_pixels_to_pixelindex_x.cl', 'set_nonzero_pixels_to_pixelindex', output.shape, parameters);
