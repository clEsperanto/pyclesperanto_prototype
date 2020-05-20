
from ..core import execute

def add_images_weighted(input1, input2, output, weight1, weight2):
    parameters = {
        "src":input1,
        "src1":input2,
        "dst":output,
        "factor":float(weight1),
        "factor1":float(weight2)
    };
    if (len(output.shape) == 2):
        execute(__file__, 'add_images_weighted_2d_x.cl', 'add_images_weighted_2d', output.shape, parameters);
    else:
        execute(__file__, 'add_images_weighted_3d_x.cl', 'add_images_weighted_3d', output.shape, parameters);
