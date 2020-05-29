from ..core import radius_to_kernel_size
from ..core import execute

def multiply_image_and_coordinate(input, output, dimension):

    parameters = {
        "src":input,
        "dst":output,
        "dimension":int(dimension)
    };

    execute(__file__, 'multiply_image_and_coordinate_' + str(len(output.shape)) + 'd_x.cl', 'multiply_image_and_coordinate_' + str(len(output.shape)) + 'd', output.shape, parameters);

