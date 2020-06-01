
from ..core import execute

def add_images_weighted(input1, input2, output, weight1, weight2):
    """
    documentation placeholder
    """


    parameters = {
        "src":input1,
        "src1":input2,
        "dst":output,
        "factor":float(weight1),
        "factor1":float(weight2)
    };

    execute(__file__, 'add_images_weighted_' + str(len(output.shape)) + 'd_x.cl', 'add_images_weighted_' + str(len(output.shape)) + 'd', output.shape, parameters);
