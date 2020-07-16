from .._tier0 import execute

def set_nonzero_pixels_to_pixelindex(input, output):
    """
    documentation placeholder
    """


    parameters = {
        "dst":output,
        "src":input
    }

    execute(__file__, 'set_nonzero_pixels_to_pixelindex_x.cl', 'set_nonzero_pixels_to_pixelindex', output.shape, parameters);
