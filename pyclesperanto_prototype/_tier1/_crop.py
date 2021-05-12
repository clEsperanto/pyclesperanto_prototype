from .._tier0 import execute
from .._tier0 import create
from .._tier0 import create_none
from .._tier0 import plugin_function
from .._tier0 import Image

@plugin_function(output_creator=create_none)
def crop(input : Image, output : Image = None, start_x : int = 0, start_y : int = 0, start_z : int = 0, width : int = 1, height : int = 1, depth : int = 1):
    """Crops a given sub-stack out of a given image stack. 
    
    Note: If the destination image pre-exists already, it will be overwritten and 
    keep it's dimensions. 
    
    Parameters
    ----------
    source : Image
    destination : Image
    start_x : Number
    start_y : Number
    start_z : Number
    width : Number
    height : Number
    depth : Number
    
    Returns
    -------
    destination
    
    Examples
    --------
    >>> import pyclesperanto_prototype as cle
    >>> cle.crop(source, destination, start_x, start_y, start_z, width, height, depth)
    
    References
    ----------
    .. [1] https://clij.github.io/clij2-docs/reference_crop3D
    """

    if output is None:
        if len(input.shape) == 2:
            output = create([height, width])
        else:
            output = create([depth, height, width])

    parameters = {
            "dst": output,
            "src": input,
            "start_x": int(start_x),
            "start_y": int(start_y),
        }
    if len(output.shape) == 3:
        # 3D image
        parameters.update({"start_z": int(start_z)})

    execute(__file__, '../clij-opencl-kernels/kernels/crop_' + str(len(output.shape)) + 'd_x.cl', 'crop_' + str(len(output.shape)) + 'd', output.shape, parameters)
    return output
