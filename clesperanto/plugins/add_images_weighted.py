
from ..core import execute
from ..core import create_like
from ..core import plugin_function
from ..core import Image

@plugin_function(output_creator=create_like)
def add_images_weighted(input1:Image, input2:Image, output:Image, weight1:float=1, weight2:float=1):
    parameters = {
        "src":input1,
        "src1":input2,
        "dst":output,
        "factor":float(weight1),
        "factor1":float(weight2)
    };

    execute(__file__, 'add_images_weighted_' + str(len(output.shape)) + 'd_x.cl', 'add_images_weighted_' + str(len(output.shape)) + 'd', output.shape, parameters);

    return output

