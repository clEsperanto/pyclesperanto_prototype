
from ..core import execute
from ..core import plugin_function
from ..core import Image
from ..core import create_like

@plugin_function(output_creator=create_like)
def apply_threshold(input:Image, output :Image = None, threshold:float=1):
    """
    Applies a user-specified threshold value to an image

    Available for: 2D, 3D

    Parameters
    ----------
    (Image , Threshold value)

    Returns
    -------
    Binary mask based on threshold value

    """


    parameters = {
        "src":input,
        "dst":output,
        "threshold":float(threshold)
    }
    execute(__file__, 'apply_threshold_' + str(len(output.shape)) + 'd.cl', 'apply_threshold_' + str(len(output.shape)) + 'd', output.shape, parameters)
    return output