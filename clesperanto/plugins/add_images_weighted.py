
from ..core import execute
from ..core import create_like
from ..core import plugin_function
from gputools import OCLArray

@plugin_function(output_creator=create_like)
def add_images_weighted(input1:OCLArray, input2:OCLArray, output:OCLArray, weight1=1, weight2=1):
    parameters = {
        "src":input1,
        "src1":input2,
        "dst":output,
        "factor":float(weight1),
        "factor1":float(weight2)
    };

    execute(__file__, 'add_images_weighted_' + str(len(output.shape)) + 'd_x.cl', 'add_images_weighted_' + str(len(output.shape)) + 'd', output.shape, parameters);

    return output

